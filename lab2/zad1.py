import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lstsq


def create_linear_representation(data, feature_columns):
    """reprezentację liniowa: kolumna jedynek (bias) + wartości cech = 5"""
    X = data[feature_columns].to_numpy()
    bias = np.ones((X.shape[0], 1))
    return np.hstack([bias, X])


def create_quadratic_representation(data, feature_columns):
    """reprezentację kwadratowa: bias, cechy (f1, f2, f3, f4) oraz
    kombinacje f1f2, f1f3, f1f4, f1^2,... = łącznie 15"""

    X = data[feature_columns].to_numpy()
    bias = np.ones((X.shape[0], 1))

    # Generujemy wszystkie kombinacje iloczynów cech (w tym kwadraty)
    quadratic_terms = []
    n_features = X.shape[1]
    for i in range(n_features):
        for j in range(i, n_features):
            quadratic_terms.append((X[:, i] * X[:, j]).reshape(-1, 1))
    quadratic_terms = np.hstack(quadratic_terms)

    return np.hstack([bias, X, quadratic_terms])


def compute_confusion_matrix(true_labels, predicted_labels):
    """tworzymy macierz pomyłek (TP, TN, FP, FN)."""
    TP = np.sum((true_labels == 1) & (predicted_labels == 1))
    TN = np.sum((true_labels == -1) & (predicted_labels == -1))
    FP = np.sum((true_labels == -1) & (predicted_labels == 1))
    FN = np.sum((true_labels == 1) & (predicted_labels == -1))
    return TP, TN, FP, FN


labels_path = "breast-cancer.labels"
train_data_path = "breast-cancer-train.dat"
validate_data_path = "breast-cancer-validate.dat"

with open(labels_path, 'r') as f:
    labels = f.read().strip().split("\n")

train_data = pd.read_csv(train_data_path, header=None, names=labels)
validate_data = pd.read_csv(validate_data_path, header=None, names=labels)

# a)
print("Dane treningowe:")
print(train_data.head())
print("\nDane walidacyjne:")
print(validate_data.head())

# b) histogram i wykres kolumny: radius (mean)
selected_column = "radius (mean)"
plt.figure(figsize=(12, 6))
train_data[train_data["Malignant/Benign"] == "M"][selected_column].hist(
    bins=30, alpha=0.7, label="Malignant"
)
train_data[train_data["Malignant/Benign"] == "B"][selected_column].hist(
    bins=30, alpha=0.7, label="Benign"
)
plt.title("Histogram of the radius (mean) divided into classes")
plt.xlabel("Radius (mean)")
plt.ylabel("Cardinality")
plt.legend()
plt.grid()
plt.show()

sorted_values = train_data[selected_column].sort_values().reset_index(drop=True)
plt.figure(figsize=(12, 6))
plt.plot(sorted_values, label=selected_column)
plt.title(f"Chart of sorted column values {selected_column}")
plt.xlabel("Index")
plt.ylabel("Radius (mean)")
plt.grid()
plt.legend()
plt.show()

# c) reprezentacja danych
# Liniowa reprezentacja: wszystkie cechy + bias
all_features = labels[2:]  # cechy (bez 'patient ID' i 'Malignant/Benign')
A_train_linear = create_linear_representation(train_data, all_features)
A_validate_linear = create_linear_representation(validate_data, all_features)

# Kwadratowa reprezentacja: bias + wybrane cechy + kombinacje iloczynów
selected_features = ["radius (mean)", "perimeter (mean)", "area (mean)", "symmetry (mean)"]
A_train_quadratic = create_quadratic_representation(train_data, selected_features)
A_validate_quadratic = create_quadratic_representation(validate_data, selected_features)

print("\nWymiary macierzy:")
print(f"A_train_linear shape: {A_train_linear.shape}")
print(f"A_train_quadratic shape: {A_train_quadratic.shape}")
print(f"A_validate_linear shape: {A_validate_linear.shape}")
print(f"A_validate_quadratic shape: {A_validate_quadratic.shape}")

# d) wektor b
b_train = np.where(train_data["Malignant/Benign"] == "M", 1, -1)
b_validate = np.where(validate_data["Malignant/Benign"] == "M", 1, -1)

# e) wagi dla reprezentacji liniowej i kwadratowej
w_linear, _, _, _ = lstsq(A_train_linear, b_train)
w_quadratic, _, _, _ = lstsq(A_train_quadratic, b_train)

print("\nWagi dla reprezentacji liniowej:")
print(w_linear)
print("\nWagi dla reprezentacji kwadratowej:")
print(w_quadratic)

# f) wagi z użyciem SVD i regularyzacji
w_linear_lstsq, residuals, rank, s = lstsq(A_train_linear, b_train)
lambda_reg = 0.01
n_features = A_train_linear.shape[1]
w_linear_reg = np.linalg.solve(A_train_linear.T @ A_train_linear + lambda_reg * np.eye(n_features),
                               A_train_linear.T @ b_train)

A_reg = A_train_linear.T @ A_train_linear + lambda_reg * np.eye(n_features)
U, S, Vt = np.linalg.svd(A_train_linear)  # dekompozycja SVD dla A_train_linear

print("\nWagi uzyskane metodą SVD (lstsq):")
print(w_linear_lstsq)
print("\nWagi uzyskane dla zregularyzowanej reprezentacji liniowej (λ = 0.01):")
print(w_linear_reg)

# g) współczynniki uwarunkowania
cond_linear = np.linalg.cond(A_train_linear.T @ A_train_linear)
cond_quad = np.linalg.cond(A_train_quadratic.T @ A_train_quadratic)
cond_linear_reg = np.linalg.cond(A_reg)  # współczynnik uwarunkowania dla liniowej
# z regularyzacją
cond_linear_svd = np.max(S) / np.min(S)

print("\nWspółczynnik uwarunkowania (liniowa metoda najmniejszych kwadratów):")
print(cond_linear)
print("\nWspółczynnik uwarunkowania (liniowa metoda najmniejszych kwadratów reg):")
print(cond_linear_reg)
print("\nWspółczynnik uwarunkowania (liniowa metoda najmniejszych kwadratów SVD):")
print(cond_linear_svd)
print("\nWspółczynnik uwarunkowania (kwadratowa metoda najmniejszych kwadratów):")
print(cond_quad)

# h) ocena modeli
p_linear = A_validate_linear @ w_linear
pred_linear = np.where(p_linear > 0, 1, -1)

p_quad = A_validate_quadratic @ w_quadratic
pred_quad = np.where(p_quad > 0, 1, -1)

TP_lin, TN_lin, FP_lin, FN_lin = compute_confusion_matrix(b_validate, pred_linear)
acc_linear = (TP_lin + TN_lin) / (TP_lin + TN_lin + FP_lin + FN_lin)

TP_quad, TN_quad, FP_quad, FN_quad = compute_confusion_matrix(b_validate, pred_quad)
acc_quad = (TP_quad + TN_quad) / (TP_quad + TN_quad + FP_quad + FN_quad)

print("\nReprezentacja liniowa:")
print(f"Macierz pomyłek: TP = {TP_lin}, TN = {TN_lin}, FP = {FP_lin}, FN = {FN_lin}")
print(f"Dokładność: {acc_linear * 100:.2f}%\n")

print("Reprezentacja kwadratowa:")
print(f"Macierz pomyłek: TP = {TP_quad}, TN = {TN_quad}, FP = {FP_quad}, FN = {FN_quad}")
print(f"Dokładność: {acc_quad * 100:.2f}%")
