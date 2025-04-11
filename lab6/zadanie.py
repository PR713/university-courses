import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from numpy.polynomial.legendre import leggauss


def f(x):
    return 4 / (1 + x ** 2)


def h_min(errors_list):
    return 1 / (n_points[np.argmin(errors_list)] - 1)


def calculate_order(error_list, n_points_list, index):
    return np.log(error_list[index - 1] / error_list[index]) / np.log(n_points_list[index] / n_points_list[index-1])
#                                                                   ^^^ h_index-1 = 1/n_points_list[index-1]


pi_exact = np.pi
print("Exact value of pi: ", pi_exact)

m_values = np.arange(1, 26)

n_points, errors_mid, errors_trapz, errors_simps = [], [], [], []

for m in m_values:
    num_points = 2 ** m + 1
    x = np.linspace(0, 1, num_points)
    h = x[1] - x[0]
    n_points.append(num_points)
    # index i is related to 2**(i+1) + 1 points

    x_mid = (x[:-1] + x[1:]) / 2
    # all points without the last one, all points without the first one
    # => intervals
    mid_val = h * np.sum(f(x_mid))
    print(f'Midpoint rule m = {m}: {mid_val}')
    error_mid = abs(mid_val - pi_exact) / pi_exact
    errors_mid.append(error_mid)

    trapz_val = integrate.trapezoid(f(x), x)
    print(f'Trapezoidal rule m = {m}: {trapz_val}')
    error_trapz = abs(trapz_val - pi_exact) / pi_exact
    errors_trapz.append(error_trapz)

    simps_val = integrate.simpson(f(x), x)
    print(f'Simpson\'s rule m = {m}: {simps_val}')
    error_simps = abs(simps_val - pi_exact) / pi_exact
    errors_simps.append(error_simps)

plt.figure(figsize=(10, 6))
plt.loglog(n_points, errors_mid, 'o-', label='Mid-point')
plt.loglog(n_points, errors_trapz, 's-', label='Trapezoidal')
plt.loglog(n_points, errors_simps, '^-', label="Simpson's")
plt.xlabel('Liczba punktów (n)')
plt.ylabel('Bezwzględny błąd względny')
plt.title('Porównanie metod kwadratur – całka ∫₀¹ 4/(1+x²) dx')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.show()

print(h_min(errors_mid))
print(h_min(errors_trapz))
print(h_min(errors_simps))

print(f"Empiryczny rząd zbieżności:")
for i in range(1, 15):
    order_mid = calculate_order(errors_mid, n_points, i)
    order_trapz = calculate_order(errors_trapz, n_points, i)

    print(f'm value: {i}')
    if i <= 6:
        order_simps = calculate_order(errors_simps, n_points, i)
        print(f"Simpson: {order_simps:.5f} (teoretycznie 4)")


    print(f"Mid-point: {order_mid:.5f} (teoretycznie 2)")
    print(f"Trapezów: {order_trapz:.5f} (teoretycznie 2)")




################zadanie 2

n_values=np.arange(2,200)   #można zmienić to 200 jak nam się podoba, liczba ewaluacji
errors_2=[]
n_evals=[]  #lista ewaluacji

for n in n_values:
    # Pobieramy węzły i wagi dla przedziału [-1, 1]
    nodes, weights = leggauss(n)
    # Mapujemy węzły na przedział [0,1]:
    #  x = 0.5*(t+1), gdzie t ∈ [-1,1]
    x_mapped = 0.5 * (nodes + 1)
    # Wagi ulegają zmianie zgodnie z dx/dt = 0.5:
    weights_mapped = 0.5 * weights

    # Obliczamy przybliżenie całki metodą Gaussa-Legendre’a:
    approx = np.sum(weights_mapped * f(x_mapped))
    print(f' Liczba ewaluacji (węzłów, pierwaistków wielomianu) {n}: {approx}')
    # Obliczamy względny błąd:
    error = abs(approx - pi_exact) / pi_exact
    errors_2.append(error)
    n_evals.append(n)

#tu nie ma sensu w ogóle liczyć h_min bo węzły do pierwiastki wielomianu Legendre'a

plt.figure(figsize=(10, 6))
plt.loglog(n_evals, errors_2, 'o-', markersize=3, label='Gauss-Legendre')
plt.xlabel('Liczba ewaluacji funkcji podcałkowej (n)')
plt.ylabel('Bezwzględny błąd względny')
plt.title('Błąd względny metody Gaussa-Legendre’a dla całki ∫₀¹ 4/(1+x²) dx')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.loglog(n_points, errors_mid, 'o-', label='Mid-point')
plt.loglog(n_points, errors_trapz, 's-', label='Trapezoidal')
plt.loglog(n_points, errors_simps, '^-', label="Simpson's")
plt.loglog(n_evals, errors_2, 'd-', label='Gauss-Legendre')
plt.xlabel('Liczba ewaluacji funkcji podcałkowej (n)')
plt.ylabel('Bezwzględny błąd względny')
plt.title('Porównanie metod kwadratur – ∫₀¹ 4/(1+x²) dx')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.show()