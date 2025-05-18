import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def euler_method(alpha, h, t_end):
    """Metoda Eulera dla równania y' = alpha*t^(alpha-1)"""
    t = np.arange(0, t_end + h, h)
    y = np.zeros_like(t)
    for i in range(1, len(t)):
        y[i] = y[i - 1] + h * alpha * t[i - 1] ** (alpha - 1)
    return t, y


def exact_solution(t, alpha):
    """Rozwiązanie dokładne y(t) = t^alpha"""
    return t ** alpha


def calculate_errors(alphas, hs, t_end=1.0):
    """Oblicza błędy i rzędy zbieżności"""
    results = {}
    for alpha in alphas:
        errors = []
        for h in hs:
            t, y_num = euler_method(alpha, h, t_end)
            y_exact = exact_solution(t, alpha)
            error = np.abs(y_num - y_exact).max()
            errors.append(error)

        # Obliczanie rzędu zbieżności
        orders = []
        for i in range(1, len(errors)):
            p = np.log(errors[i] / errors[i - 1]) / np.log(hs[i] / hs[i - 1])
            orders.append(p)

        results[alpha] = {'errors': errors, 'orders': orders}
    return results


def plot_results(alphas, hs, results):
    """Generuje wykresy błędów i rozwiązań"""
    plt.figure(figsize=(15, 10))

    # Wykres błędów
    plt.subplot(2, 2, 1)
    for alpha in alphas:
        plt.loglog(hs, results[alpha]['errors'], 'o-', label=f'α={alpha}')
    plt.xlabel('Krok h')
    plt.ylabel('Maksymalny błąd')
    plt.title('Zależność błędu od kroku h')
    plt.legend()
    plt.grid(True, which="both", ls="-")

    # Wykres rozwiązań dla h=0.1
    plt.subplot(2, 2, 2)
    t_fine = np.linspace(0, 1, 100)
    for alpha in alphas:
        # Rozwiązanie dokładne
        plt.plot(t_fine, exact_solution(t_fine, alpha), '--', label=f'Dokładne α={alpha}')
        # Rozwiązanie numeryczne
        t, y_num = euler_method(alpha, 0.1, 1.0)
        plt.plot(t, y_num, 'o-', label=f'Numeryczne α={alpha}')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title('Porównanie rozwiązań (h=0.1)')
    plt.legend()
    plt.grid()

    # Wykres rzędów zbieżności
    plt.subplot(2, 2, 3)
    for alpha in alphas:
        orders = results[alpha]['orders']
        h_pairs = [f"{hs[i]}/{hs[i + 1]}" for i in range(len(hs) - 1)]
        plt.plot(h_pairs, orders, 's-', label=f'α={alpha}')
    plt.xlabel('Pary kroków h')
    plt.ylabel('Empiryczny rząd zbieżności')
    plt.title('Rząd zbieżności metody')
    plt.axhline(y=1, color='r', linestyle='--', label='Teoretyczny rząd=1')
    plt.legend()
    plt.grid()
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.tight_layout()
    plt.show()


# Parametry
alphas = [2.5, 1.5, 1.1]
hs = [0.2, 0.1, 0.05]

# Obliczenia
results = calculate_errors(alphas, hs)

# Wyświetlenie wyników
print("Błędy i rzędy zbieżności:")
for alpha in alphas:
    print(f"\nα = {alpha}")
    for i, h in enumerate(hs):
        print(f"h = {h:.3f}, Błąd = {results[alpha]['errors'][i]:.6f}")
    for i, order in enumerate(results[alpha]['orders']):
        print(f"Rząd zbieżności dla h={hs[i]}/{hs[i + 1]}: {order:.4f}")

# Generowanie wykresów
plot_results(alphas, hs, results)