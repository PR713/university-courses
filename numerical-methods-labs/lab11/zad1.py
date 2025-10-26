import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt


# --- Funkcje pomocnicze z Laboratorium 2 ---

def create_linear_representation(data, feature_columns):
    X = data[feature_columns].to_numpy()

    X = (X - X.mean(axis=0)) / X.std(axis=0)
    bias = np.ones((X.shape[0], 1))
    return np.hstack([bias, X])


def compute_accuracy(A_validate, b_validate, w):
    p = A_validate @ w
    predictions = np.where(p > 0, 1, -1)

    TP = np.sum((b_validate == 1) & (predictions == 1))
    TN = np.sum((b_validate == -1) & (predictions == -1))
    FP = np.sum((b_validate == -1) & (predictions == 1))
    FN = np.sum((b_validate == 1) & (predictions == -1))

    accuracy = (TP + TN) / (TP + TN + FP + FN)
    return accuracy, (TP, TN, FP, FN)


# --- Implementacja Metody Spadku Wzdłuż Gradientu ---

def gradient_descent(A, b, learning_rate, n_iterations):
    w = np.zeros(A.shape[1])
    m = len(b)
    cost_history = []

    for i in range(n_iterations):
        predictions = A @ w
        error = predictions - b


        cost = np.mean(error ** 2)
        cost_history.append(cost)


        gradient = (2 / m) * A.T @ error
        w = w - learning_rate * gradient

    return w, cost_history


# --- Główny skrypt ---

# 1. Wczytanie i przygotowanie danych
try:
    with open("breast-cancer.labels", 'r') as f:
        labels = f.read().strip().split("\n")
    train_data = pd.read_csv("breast-cancer-train.dat", header=None, names=labels)
    validate_data = pd.read_csv("breast-cancer-validate.dat", header=None, names=labels)
except FileNotFoundError:
    print(
        "Błąd: Pliki danych ('breast-cancer-train.dat', 'breast-cancer-validate.dat', 'breast-cancer.labels') nie zostały znalezione.")
    print("Upewnij się, że znajdują się w tym samym katalogu co skrypt.")
    exit()

# Przygotowanie macierzy A i wektora b
all_features = labels[2:]
A_train = create_linear_representation(train_data, all_features)
A_validate = create_linear_representation(validate_data, all_features)
b_train = np.where(train_data["Malignant/Benign"] == "M", 1, -1)
b_validate = np.where(validate_data["Malignant/Benign"] == "M", 1, -1)

# --- WYKRES 1: Histogram wybranej cechy (z Lab 2) ---
plt.figure(figsize=(10, 6))
selected_column = "radius (mean)"
plt.hist(train_data[train_data["Malignant/Benign"] == "M"][selected_column], bins=30, alpha=0.7,
         label="Złośliwy (Malignant)")
plt.hist(train_data[train_data["Malignant/Benign"] == "B"][selected_column], bins=30, alpha=0.7,
         label="Łagodny (Benign)")
plt.title(f'Histogram cechy "{selected_column}"')
plt.xlabel(f'Wartość cechy "{selected_column}"')
plt.ylabel("Liczba przypadków")
plt.legend()
plt.grid(True)
plt.show()

# --- Porównanie metod ---
print("Rozpoczynam porównanie metody najmniejszych kwadratów i spadku wzdłuż gradientu.\n")

# 2. Metoda Najmniejszych Kwadratów (równanie normalne)
print("--- Metoda Najmniejszych Kwadratów (Równanie Normalne) ---")
start_time_ls = time.time()
AtA = A_train.T @ A_train
Atb = A_train.T @ b_train
w_ls = np.linalg.solve(AtA, Atb)
end_time_ls = time.time()
time_ls = end_time_ls - start_time_ls
acc_ls, _ = compute_accuracy(A_validate, b_validate, w_ls)
print(f"Dokładność na zbiorze testowym: {acc_ls * 100:.2f}%")
print(f"Czas obliczeń: {time_ls:.6f} s\n")

# 3. Metoda Spadku Wzdłuż Gradientu
print("--- Metoda Spadku Wzdłuż Gradientu ---")
AtA_gd = A_train.T @ A_train
eigenvalues = np.linalg.eigvalsh(AtA_gd)
lambda_max = np.max(eigenvalues)
learning_rate = 1.9 / lambda_max
print(f"Wyznaczona stała ucząca (alpha): {learning_rate:.4f}")

n_iterations = 1000
start_time_gd = time.time()
w_gd, cost_history = gradient_descent(A_train, b_train, learning_rate, n_iterations)
end_time_gd = time.time()
time_gd = end_time_gd - start_time_gd
acc_gd, _ = compute_accuracy(A_validate, b_validate, w_gd)
print(f"Liczba iteracji: {n_iterations}")
print(f"Dokładność na zbiorze testowym: {acc_gd * 100:.2f}%")
print(f"Czas obliczeń: {time_gd:.6f} s\n")

# --- WYKRES 2: Funkcja kosztu w czasie dla spadku gradientu ---
plt.figure(figsize=(10, 6))
plt.plot(range(n_iterations), cost_history)
plt.title("Zmiana funkcji kosztu w trakcie treningu (Gradient Descent)")
plt.xlabel("Iteracja")
plt.ylabel("Koszt (Błąd Średniokwadratowy)")
plt.grid(True)
plt.show()

# --- WYKRES 3: Porównanie wag obu modeli ---
plt.figure(figsize=(15, 7))
x = np.arange(len(w_ls))
width = 0.35
plt.bar(x - width / 2, w_ls, width, label='Metoda Najmniejszych Kwadratów (LS)')
plt.bar(x + width / 2, w_gd, width, label='Spadek Wzdłuż Gradientu (GD)')
plt.title("Porównanie wag (w) dla obu metod")
plt.xlabel("Indeks cechy (0 to bias)")
plt.ylabel("Wartość wagi")
plt.xticks(x)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# --- WYKRES 4: Histogramy rozkładu predykcji ---
p_ls = A_validate @ w_ls
p_gd = A_validate @ w_gd

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), sharey=True, sharex=True)

# Histogram dla Metody Najmniejszych Kwadratów
ax1.hist(p_ls[b_validate == 1], bins=20, alpha=0.7, label='Prawdziwe: Złośliwy')
ax1.hist(p_ls[b_validate == -1], bins=20, alpha=0.7, label='Prawdziwe: Łagodny')
ax1.axvline(0, color='red', linestyle='--', label='Granica decyzyjna (p=0)')
ax1.set_title('Rozkład predykcji - Metoda LS')
ax1.set_xlabel('Wynik predykcji (p = A*w)')
ax1.set_ylabel('Liczba przypadków')
ax1.legend()
ax1.grid(True)

# Histogram dla Metody Spadku Gradientu
ax2.hist(p_gd[b_validate == 1], bins=20, alpha=0.7, label='Prawdziwe: Złośliwy')
ax2.hist(p_gd[b_validate == -1], bins=20, alpha=0.7, label='Prawdziwe: Łagodny')
ax2.axvline(0, color='red', linestyle='--', label='Granica decyzyjna (p=0)')
ax2.set_title('Rozkład predykcji - Metoda GD')
ax2.set_xlabel('Wynik predykcji (p = A*w)')
ax2.legend()
ax2.grid(True)

plt.suptitle("Histogramy rozkładu predykcji na zbiorze walidacyjnym", fontsize=16)
plt.show()

# --- Podsumowanie końcowe ---
print("\n================ PODSUMOWANIE ================")
print(f"{'Kryterium':<30} | {'Metoda Najmniejszych Kwadratów':<35} | {'Spadek Wzdłuż Gradientu':<30}")
print("-" * 95)
print(f"{'Dokładność na zbiorze testowym':<30} | {f'{acc_ls * 100:.2f}%':<35} | {f'{acc_gd * 100:.2f}%':<30}")
print(f"{'Czas obliczeń':<30} | {f'{time_ls:.6f} s':<35} | {f'{time_gd:.6f} s':<30}")
print("\n--- Teoretyczna złożoność obliczeniowa ---")
print("Zakładając, że macierz A ma wymiary n x m (n - próbki, m - cechy):\n")
print("Metoda Najmniejszych Kwadratów (Równanie Normalne):")
print(" - Obliczenie A.T @ A: O(n * m^2)")
print(" - Rozwiązanie układu równań (np. dekompozycja Cholesky'ego): O(m^3)")
print(" - Dominująca złożoność: O(n * m^2 + m^3)")
print(" - Jest to metoda dokładna, ale kosztowna obliczeniowo, gdy liczba cech (m) jest duża.\n")
print("Metoda Spadku Wzdłuż Gradientu:")
print(" - Obliczenie gradientu w jednej iteracji: O(n * m)")
print(" - Całkowita złożoność dla k iteracji: O(k * n * m)")
print(
    " - Jest to metoda iteracyjna. Staje się bardziej efektywna od równań normalnych, gdy liczba cech (m) jest bardzo duża, ponieważ unika kosztownej operacji O(m^3).")
print("============================================")