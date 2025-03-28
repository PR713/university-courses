import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.legendre import legroots
from scipy.interpolate import CubicSpline

"""
EFEKT RUNGEGO - IMPLEMENTACJA Z MANUALNĄ INTERPOLACJĄ LAGRANGE'A

1. Analiza rozkładu punktów poprzez średnią geometryczną odległości
2. Porównanie metod interpolacji dla funkcji Rungego i exp(cos(x))
"""


def geometric_mean_distance(points):
    """
    Oblicza średnią geometryczną odległości każdego punktu do pozostałych
    points -- wektor punktów (np.array)
    """
    n = len(points)
    result = np.zeros(n)

    for i in range(n):
        distances = np.abs(points[i] - np.delete(points, i))
        result[i] = np.exp(np.mean(np.log(distances)))

    return result


def manual_lagrange(x_points, y_points, x_eval):
    """
    Manualna implementacja interpolacji Lagrange'a
    x_points: węzły interpolacji
    y_points: wartości funkcji w węzłach
    x_eval: punkty do obliczenia wartości wielomianu
    """
    n = len(x_points)
    result = np.zeros_like(x_eval)

    for i in range(n):
        term = np.ones_like(x_eval)
        for j in range(n):
            if i != j:
                term *= (x_eval - x_points[j]) / (x_points[i] - x_points[j])
        result += y_points[i] * term

    return result


def zadanie1():
    ns = [10, 20, 50]

    fig, axes = plt.subplots(3, 1, figsize=(10, 12))
    plt.suptitle('Średnie geometryczne odległości dla różnych rozkładów punktów', y=1.02)

    for i, n in enumerate(ns):
        chebyshev = -np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))
        legendre_points = legroots([0] * n + [1])
        legendre_points.sort()
        uniform = np.linspace(-1, 1, n)

        cheb_dist = geometric_mean_distance(chebyshev)
        leg_dist = geometric_mean_distance(legendre_points)
        uni_dist = geometric_mean_distance(uniform)

        ax = axes[i]
        ax.plot(chebyshev, cheb_dist, 'ro', label=f'Czebyszewa n={n}')
        ax.plot(legendre_points, leg_dist, 'g^', label=f'Legendre n={n}')
        ax.plot(uniform, uni_dist, 'bs', label=f'Równomierne n={n}')

        ax.set_xlabel('Punkty x_j', fontsize=10)
        ax.set_ylabel('Średnia geometryczna odległości', fontsize=10)
        ax.set_title(f'Porównanie dla n={n}', fontsize=12)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def zadanie2():
    def f1(x):
        return 1 / (1 + 25 * x ** 2)

    def f2(x):
        return np.exp(np.cos(x))

    # a)
    n = 12

    x_uniform = np.linspace(-1, 1, n)
    y_uniform = f1(x_uniform)

    theta = (2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n)
    x_cheb = -np.cos(theta)
    y_cheb = f1(x_cheb)

    x_eval_uniform = np.linspace(-1, 1, 120)
    x_eval_cheb = -np.cos(np.linspace(0, np.pi, 120))

    # Manualna interpolacja Lagrange'a
    lagrange_uni = manual_lagrange(x_uniform, y_uniform, x_eval_uniform)
    lagrange_cheb = manual_lagrange(x_cheb, y_cheb, x_eval_cheb)

    cs_uniform = CubicSpline(x_uniform, y_uniform)

    plt.figure(figsize=(12, 6))
    plt.plot(x_eval_uniform, f1(x_eval_uniform), 'k-', linewidth=2,
             label='Funkcja dokładna')
    plt.plot(x_eval_uniform, lagrange_uni, 'r--', linewidth=1.5,
             label='Lagrange równomierny')
    plt.plot(x_eval_cheb, lagrange_cheb, 'b--', linewidth=1.5,
             label='Lagrange Czebyszew')
    plt.plot(x_eval_uniform, cs_uniform(x_eval_uniform), 'g--', linewidth=1.5,
             label='Cubic spline równomierny')

    plt.scatter(x_uniform, y_uniform, c='red', marker='o', s=50,
                label='Węzły równomierne')
    plt.scatter(x_cheb, y_cheb, c='blue', marker='x', s=50,
                label='Węzły Czebyszewa')

    plt.xlabel('x', fontsize=12)
    plt.ylabel('f(x)', fontsize=12)
    plt.title('Interpolacja funkcji Rungego f1(x) = 1/(1+25x²) dla n=12', fontsize=14)
    plt.legend(fontsize=10, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.show()

    # b)
    ns = range(4, 51)
    num_test_points = 500

    errors_f1 = {'uniform_lag': [], 'cheb_lag': [], 'uniform_cs': []}
    errors_f2 = {'uniform_lag': [], 'cheb_lag': [], 'uniform_cs': []}

    for n in ns:
        x_test = np.random.uniform(-1, 1, num_test_points)
        y_true = f1(x_test)

        # Lagrange równomierny
        x_uni = np.linspace(-1, 1, n)
        y_uni = f1(x_uni)
        y_pred = manual_lagrange(x_uni, y_uni, x_test)
        errors_f1['uniform_lag'].append(np.linalg.norm(y_pred - y_true))

        # Lagrange Czebyszew
        theta = (2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n)
        x_cheb = -np.cos(theta)
        y_cheb = f1(x_cheb)
        y_pred = manual_lagrange(x_cheb, y_cheb, x_test)
        errors_f1['cheb_lag'].append(np.linalg.norm(y_pred - y_true))

        # Cubic spline równomierny
        cs = CubicSpline(x_uni, y_uni)
        y_pred = cs(x_test)
        errors_f1['uniform_cs'].append(np.linalg.norm(y_pred - y_true))

        # f2 - punkty w [0, 2π]
        x_test = np.random.uniform(0, 2 * np.pi, num_test_points)
        y_true = f2(x_test)

        # Lagrange równomierny
        x_uni = np.linspace(0, 2 * np.pi, n)
        y_uni = f2(x_uni)
        y_pred = manual_lagrange(x_uni, y_uni, x_test)
        errors_f2['uniform_lag'].append(np.linalg.norm(y_pred - y_true))

        # Lagrange Czebyszew (przeskalowany do [0, 2π])
        x_cheb = np.pi * (1 - np.cos(theta))
        y_cheb = f2(x_cheb)
        y_pred = manual_lagrange(x_cheb, y_cheb, x_test)
        errors_f2['cheb_lag'].append(np.linalg.norm(y_pred - y_true))

        # Cubic spline równomierny
        cs = CubicSpline(x_uni, y_uni)
        y_pred = cs(x_test)
        errors_f2['uniform_cs'].append(np.linalg.norm(y_pred - y_true))

    # WYKRESY BŁĘDÓW
    # Dla funkcji f1
    plt.figure(figsize=(12, 6))
    plt.plot(ns, errors_f1['uniform_lag'], 'r-', label='Lagrange równomierny')
    plt.plot(ns, errors_f1['cheb_lag'], 'b-', label='Lagrange Czebyszew')
    plt.plot(ns, errors_f1['uniform_cs'], 'g-', label='Cubic spline równomierny')

    plt.xlabel('Liczba węzłów interpolacji (n)', fontsize=12)
    plt.ylabel('Norma błędu interpolacji', fontsize=12)
    plt.title('Błędy interpolacji funkcji Rungego f1(x) = 1/(1+25x²)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.show()

    # Dla funkcji f2
    plt.figure(figsize=(12, 6))
    plt.plot(ns, errors_f2['uniform_lag'], 'r-', label='Lagrange równomierny')
    plt.plot(ns, errors_f2['cheb_lag'], 'b-', label='Lagrange Czebyszew')
    plt.plot(ns, errors_f2['uniform_cs'], 'g-', label='Cubic spline równomierny')

    plt.xlabel('Liczba węzłów interpolacji (n)', fontsize=12)
    plt.ylabel('Norma błędu interpolacji', fontsize=12)
    plt.title('Błędy interpolacji funkcji f2(x) = exp(cos(x))', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.show()


print("=== ZADANIE 1 ===")
zadanie1()
print("\n=== ZADANIE 2 ===")
zadanie2()