import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss


def f(x):
    return 4 / (1 + x ** 2)


# Dokładna wartość π
pi_exact = np.pi

# ======================================================================
# Część z poprzedniego laboratorium (identyczna jak w oryginalnym kodzie)
# ======================================================================

m_values = np.arange(1, 26)
n_points, errors_mid, errors_trapz, errors_simps = [], [], [], []

for m in m_values:
    num_points = 2 ** m + 1
    x = np.linspace(0, 1, num_points)
    h = x[1] - x[0]  # Poprawione: obliczamy h jako różnicę między punktami
    n_points.append(num_points)

    # Metoda punktu środkowego (taka sama jak w oryginalnym kodzie)
    x_mid = (x[:-1] + x[1:]) / 2
    mid_val = h * np.sum(f(x_mid))
    error_mid = abs(mid_val - pi_exact) / pi_exact
    errors_mid.append(error_mid)

    # Metoda trapezów
    trapz_val = integrate.trapezoid(f(x), x)
    error_trapz = abs(trapz_val - pi_exact) / pi_exact
    errors_trapz.append(error_trapz)

    # Metoda Simpsona
    simps_val = integrate.simpson(f(x), x)
    error_simps = abs(simps_val - pi_exact) / pi_exact
    errors_simps.append(error_simps)

# Metoda Gaussa-Legendre'a (identyczna jak w oryginalnym kodzie)
n_values = np.arange(2, 200)
errors_gl, n_evals_gl = [], []
for n in n_values:
    nodes, weights = leggauss(n)
    x_mapped = 0.5 * (nodes + 1)
    weights_mapped = 0.5 * weights
    approx = np.sum(weights_mapped * f(x_mapped))
    error = abs(approx - pi_exact) / pi_exact
    errors_gl.append(error)
    n_evals_gl.append(n)


# ======================================================================
# Nowa część - adaptacyjne metody (bez zmian)
# ======================================================================

def adaptive_trapezoid(f, a, b, tol_abs):
    stack = [(a, b, f(a), f(b))]
    neval = 2
    integral = 0.0
    while stack:
        a, b, fa, fb = stack.pop()
        c = (a + b) / 2
        fc = f(c)
        neval += 1
        h = b - a
        integral_single = h * (fa + fb) / 2
        integral_left = (c - a) * (fa + fc) / 2
        integral_right = (b - c) * (fc + fb) / 2
        integral_double = integral_left + integral_right
        error = abs(integral_double - integral_single)
        if error <= tol_abs:
            integral += integral_double
        else:
            stack.append((c, b, fc, fb))
            stack.append((a, c, fa, fc))
    return integral, neval


tolerances = np.logspace(0, -14, num=15)
nevals_trap, errors_trap = [], []
nevals_gk, errors_gk = [], []

for tol in tolerances:
    # Adaptacyjne trapezy
    tol_abs = tol * pi_exact
    result, neval = adaptive_trapezoid(f, 0, 1, tol_abs)
    err = abs(result - pi_exact) / pi_exact
    nevals_trap.append(neval)
    errors_trap.append(err)

    # Gauss-Kronrod
    result, _, info = quad(f, 0, 1, epsrel=tol, full_output=True)
    neval = info['neval']
    err = abs(result - pi_exact) / pi_exact
    nevals_gk.append(neval)
    errors_gk.append(err)

# ======================================================================
# Wykresy (z poprawionymi etykietami i stylami)
# ======================================================================

plt.figure(figsize=(12, 8))
# Metody nieadaptacyjne
plt.loglog(n_points, errors_mid, 'o-', label='Mid-point (złożona)', markersize=5, alpha=0.7)
plt.loglog(n_points, errors_trapz, 's-', label='Trapezoidalna (złożona)', markersize=5, alpha=0.7)
plt.loglog(n_points, errors_simps, '^-', label="Simpsona (złożona)", markersize=5, alpha=0.7)
plt.loglog(n_evals_gl, errors_gl, 'd-', label='Gauss-Legendre', markersize=4, alpha=0.7)

# Metody adaptacyjne
plt.loglog(nevals_trap, errors_trap, 'p-', label='Adapt. trapezoidalna', markersize=8)
plt.loglog(nevals_gk, errors_gk, '*-', label='Gauss-Kronrod (quad)', markersize=8)

plt.xlabel('Liczba ewaluacji funkcji podcałkowej', fontsize=12)
plt.ylabel('Bezwzględny błąd względny', fontsize=12)
plt.title('Porównanie metod całkowania numerycznego\n∫₀¹ 4/(1+x²) dx', fontsize=14)
plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()