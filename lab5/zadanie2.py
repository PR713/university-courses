import numpy as np
import matplotlib.pyplot as plt

# Funkcja, którą chcemy aproksymować: f(x) = sqrt(x) na [0,2]
def f(x):
    return np.sqrt(x)

# Transformacja o wektor T = [-1,0], przekształcamy przedział OX [0,2] do [-1,1]
# tak że wartości z [-1,1] odpowiadają wartościom w punktach z przedziału [0,2]
def g(y):
    return np.sqrt(y + 1)  # g(y) = f(y+1)

# Definicja wielomianów Czebyszewa pierwszego rodzaju:
def T0(y):
    return np.ones_like(y)

def T1(y):
    return y

def T2(y):
    return 2 * y**2 - 1

# Lista funkcji reprezentujących kolejne wielomiany Czebyszewa
T_funcs = [T0, T1, T2]

# Liczba punktów do kwadratury Gaussa-Czebyszewa (im więcej, tym dokładniej)
n_points = 100
# Uzyskujemy węzły i wagi dla kwadratury Gaussa-Czebyszewa
# Dla całki postaci: ∫[-1,1] f(y)/sqrt(1-y^2) dy,
# wagi w Gaussie Czebyszewa są równe: w_j = π/n_points.
y_nodes, _ = np.polynomial.chebyshev.chebgauss(n_points)
w = np.full(n_points, np.pi/n_points)  # wsz

# ystkie wagi

# Obliczanie współczynników c_k dla k = 0, 1, 2:
c = np.zeros(3)
for k in range(3):
    # Obliczamy całkę ∫[-1,1] g(y) T_k(y)/sqrt(1-y^2) dy przy użyciu kwadratury Gaussa-Czebyszewa
    integrand = g(y_nodes) * T_funcs[k](y_nodes)
    integral = np.sum(w * integrand)  # suma wagowa
    # Uwzględniamy współczynnik (2 - δ_k0)/π:
    c[k] = (2 - (k==0)) * integral / np.pi

print("Współczynniki szeregowe (w bazie Czebyszewa):")
for k in range(3):
    print(f"c_{k} = {c[k]:.6f}")

# Utworzenie aproksymacji w postaci szeregu Czebyszewa
# g_approx(y) = c0*T0(y) + c1*T1(y) + c2*T2(y)
def g_approx(y):
    return c[0]*T0(y) + c[1]*T1(y) + c[2]*T2(y)

# Przekształcenie aproksymacji do postaci funkcji w x: x = y+1, czyli
# P(x) = g_approx(x-1)
def P(x):
    return g_approx(x - 1)

# Test: porównanie f(x) i P(x) na przedziale [0,2]
x_vals = np.linspace(0, 2, 200)
f_vals = f(x_vals)
P_vals = P(x_vals)

# Wykres porównawczy
plt.figure(figsize=(8, 5))
plt.plot(x_vals, f_vals, label='f(x) = √x', linewidth=2)
plt.plot(x_vals, P_vals, label='Aproksymacja Czebyszewa (stopień 2)', linestyle='--', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja średniokwadratowa ciągła funkcji √x')
plt.legend()
plt.grid(True)
plt.show()

# Obliczenie błędu aproksymacji (np. normy L2 na przedziale [0,2])
error = np.sqrt(np.trapezoid((f_vals - P_vals)**2, x_vals))
print(f"Błąd aproksymacji (L2): {error:.6f}")
