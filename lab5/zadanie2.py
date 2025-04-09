import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(x)

# Transformacja o wektor T = [-1,0], przekształcamy przedział OX [0,2] do [-1,1]
# tak że wartości z [-1,1] odpowiadają wartościom w punktach z przedziału [0,2]
def g(y):
    return np.sqrt(y + 1)  # g(y) = f(y+1)

def T0(y):
    return np.ones_like(y)

def T1(y):
    return y

def T2(y):
    return 2 * y**2 - 1

# Lista funkcji reprezentujących kolejne wielomiany Czebyszewa
T_funcs = [T0, T1, T2]

n_points = 100
y_nodes, _ = np.polynomial.chebyshev.chebgauss(n_points)
w = np.full(n_points, np.pi/n_points)  # wszystkie wagi

# Obliczanie współczynników c_k dla k = 0, 1, 2:
c = np.zeros(3)
for k in range(3):
    integrand = g(y_nodes) * T_funcs[k](y_nodes)
    integral = np.sum(w * integrand)
    c[k] = (2 - (k==0)) * integral / np.pi

print("Współczynniki szeregowe (w bazie Czebyszewa):")
for k in range(3):
    print(f"c_{k} = {c[k]:.6f}")

def g_approx(y):
    return c[0]*T0(y) + c[1]*T1(y) + c[2]*T2(y)

def P(x):
    return g_approx(x - 1)

x_vals = np.linspace(0, 2, 200)
f_vals = f(x_vals)
P_vals = P(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, f_vals, label='f(x) = √x', linewidth=2)
plt.plot(x_vals, P_vals, label='Aproksymacja Czebyszewa (stopień 2)', linestyle='--', linewidth=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja średniokwadratowa ciągła funkcji √x')
plt.legend()
plt.grid(True)
plt.show()

error = np.sqrt(np.trapezoid((f_vals - P_vals)**2, x_vals))
print(f"Błąd aproksymacji (L2): {error:.6f}")
