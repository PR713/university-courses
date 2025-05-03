import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

def f1(x):
    return 4 / (1 + x ** 2)


def f2(x):
    """Osobliwość w x=0, ale całka na [0,1] istnieje i wynosi -4/9.
    Teraz działa zarówno dla skalarnych x, jak i tablic NumPy."""
    if isinstance(x, (np.ndarray, list)):
        #dla tablic
        with np.errstate(divide='ignore', invalid='ignore'):
            result = np.sqrt(x) * np.log(x)
            result[x == 0] = 0 #granica z tw. D'Hospitala -> 0
        return result
    else:
        #dla pojedynczych wartości
        if x == 0:
            return 0.0
        with np.errstate(divide='ignore', invalid='ignore'):
            return np.sqrt(x) * np.log(x)


# Parametry dla f3
a = 0.001
b = 0.004


def f3(x):
    """Funkcja podcałkowa z pikami w x=0.3 i x=0.9.
    Wartość dokładna nieznana analitycznie - obliczana numerycznie."""
    return 1 / ((x - 0.3) ** 2 + a) + 1 / ((x - 0.9) ** 2 + b) - 6


functions = [f1, f2, f3]
labels = [
    "∫₀¹ 4/(1+x²) dx (π)",
    "∫₀¹ √x log(x) dx (-4/9)",
    "∫₀¹ (1/((x-0.3)²+a) + 1/((x-0.9)²+b) - 6) dx"
]
exact_values = [np.pi, -4 / 9, None]  # Dla trzeciej funkcji obliczymy wartość numerycznie


m_values = np.arange(1, 17)  # Dla metod złożonych (2^m + 1 punktów)
n_values = np.arange(2, 80)  # Dla kwadratury Gaussa-Legendre'a
tolerances = np.logspace(0, -14, num=12)  # Tolerancje dla metod adaptacyjnych


# Adaptacyjna metoda trapezów
def adaptive_trapezoid(f, a, b, tol_abs, max_iter=10000):
    """Adaptacyjna całkowanie metodą trapezów z kontrolą błędu.
        f: funkcja podcałkowa (musi obsługiwać pojedyncze wartości)
        a, b: granice całkowania
        tol_abs: tolerancja absolutna błędu
        max_iter: zabezpieczenie przed nieskończoną pętlą

    zwraca:
        (wartość całki, liczba ewaluacji funkcji)
    """
    # Sprawdzenie wartości na granicach
    fa = f(a)
    fb = f(b)
    stack = [(a, b, fa, fb)]
    neval = 2
    integral = 0.0
    iteration = 0

    while stack and iteration < max_iter:
        iteration += 1
        a, b, fa, fb = stack.pop()
        c = (a + b) / 2
        fc = f(c)
        neval += 1

        # Oblicz całkę dla pojedynczego i podwójnego przedziału
        h = b - a
        integral_single = h * (fa + fb) / 2
        integral_double = h * (fa + 2 * fc + fb) / 4

        # Estymator błędu
        error = abs(integral_double - integral_single)

        if error <= tol_abs:
            integral += integral_double
        else:
            stack.append((c, b, fc, fb))
            stack.append((a, c, fa, fc))

    if iteration >= max_iter:
        print(f"Ostrzeżenie: osiągnięto maksymalną liczbę iteracji ({max_iter})")

    return integral, neval



for idx, (f, label, exact) in enumerate(zip(functions, labels, exact_values)):
    print(f"\n==== Obliczenia dla: {label} ====")

    # Oblicz wartość dokładną dla trzeciej funkcji
    if exact is None:
        exact, _ = quad(f, 0, 1, epsrel=1e-14)
        print(f"Wartość dokładna (numerycznie): {exact:.15f}")

    n_points, errors_mid, errors_trapz, errors_simps = [], [], [], []

    # Metody złożone: punkt środkowy, trapezowa, Simpsona
    for m in m_values:
        num_points = 2 ** m + 1
        x = np.linspace(0, 1, num_points)
        h = x[1] - x[0]
        n_points.append(num_points)

        # Metoda punktu środkowego
        x_mid = (x[:-1] + x[1:]) / 2
        mid_val = h * np.sum(f(x_mid))
        errors_mid.append(abs(mid_val - exact) / abs(exact))

        # Metoda trapezów
        trapz_val = integrate.trapezoid(f(x), x)
        errors_trapz.append(abs(trapz_val - exact) / abs(exact))

        # Metoda Simpsona
        simps_val = integrate.simpson(f(x), x)
        errors_simps.append(abs(simps_val - exact) / abs(exact))

    # Kwadratura Gaussa-Legendre'a
    errors_gl, n_evals_gl = [], []
    for n in n_values:
        nodes, weights = leggauss(n)
        x_mapped = 0.5 * (nodes + 1)  # Przeskalowanie z [-1,1] na [0,1]
        weights_mapped = 0.5 * weights
        approx = np.sum(weights_mapped * f(x_mapped))
        errors_gl.append(abs(approx - exact) / abs(exact))
        n_evals_gl.append(n)

    # Metody adaptacyjne
    nevals_trap, errors_trap = [], []
    nevals_gk, errors_gk = [], []
    for tol in tolerances:
        # Adaptacyjna metoda trapezów
        tol_abs = tol * abs(exact)
        result, neval = adaptive_trapezoid(f, 0, 1, tol_abs)
        nevals_trap.append(neval)
        errors_trap.append(abs(result - exact) / abs(exact))

        # Adaptacyjna metoda Gaussa-Kronroda (scipy.quad)
        result, _, info = quad(f, 0, 1, epsrel=tol, full_output=True)
        err = abs(result - exact) / abs(exact)
        nevals_gk.append(info['neval'])
        errors_gk.append(err)


#wizualizacja
    plt.figure(figsize=(12, 8))

    # Metody złożone
    plt.loglog(n_points, errors_mid, 'o-', label='Punkt środkowy (złożony)', alpha=0.7)
    plt.loglog(n_points, errors_trapz, 's-', label='Trapezowa (złożona)', alpha=0.7)
    plt.loglog(n_points, errors_simps, '^-', label="Simpsona (złożona)", alpha=0.7)

    # Kwadratura Gaussa
    plt.loglog(n_evals_gl, errors_gl, 'd-', label='Gauss-Legendre', alpha=0.7)

    # Metody adaptacyjne
    plt.loglog(nevals_trap, errors_trap, 'p-', label='Adapt. trapezowa', markersize=8)
    plt.loglog(nevals_gk, errors_gk, '*-', label='Gauss-Kronrod (quad)', markersize=8)

    plt.xlabel('Liczba ewaluacji funkcji', fontsize=12)
    plt.ylabel('Błąd względny', fontsize=12)
    plt.title(f'Porównanie metod całkowania numerycznego\n{label}', fontsize=14)
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()