import numpy as np
import matplotlib.pyplot as plt

# Dokładny pierwiastek
x_star = 2.0


# Funkcje iteracyjne
def phi1(x):
    return (x ** 2 + 2) / 3


def phi2(x):
    return np.sqrt(3 * x - 2)


def phi3(x):
    return 3 - 2 / x


def phi4(x):
    denominator = 2 * x - 3
    if abs(denominator) < 1e-10:
        return x_star
    return (x ** 2 - 2) / denominator


# Pochodne funkcji iteracyjnych
def phi1_prime(x):
    return (2 * x) / 3


def phi2_prime(x):
    return 3 / (2 * np.sqrt(3 * x - 2))


def phi3_prime(x):
    return 2 / (x ** 2)


def phi4_prime(x):
    return (2 * x * (2 * x - 3) - 2 * (x ** 2 - 2)) / ((2 * x - 3) ** 2)


print("Wartości pochodnych w x=2:")
print(f"φ1': {phi1_prime(2)}")  # 4/3 ≈ 1.333 > 1 - rozbieżna
print(f"φ2': {phi2_prime(2)}")  # 3/(2*2) = 0.75 < 1 - zbieżna liniowo
print(f"φ3': {phi3_prime(2)}")  # 2/4 = 0.5 < 1 - zbieżna liniowo
print(f"φ4': {phi4_prime(2)}")  # φ4'(2)=0 - zbieżna co najmniej kwadratowo



def iterative_method(phi, x0, iterations=10):
    x = x0
    history = [x]
    errors = [abs(x - x_star)]

    for _ in range(iterations):
        x = phi(x)
        history.append(x)
        errors.append(abs(x - x_star))

    return history, errors


# Parametry początkowe
x0 = 2.6 # Punkt startowy blisko pierwiastka 2
iterations = 10

methods = {
    'φ1(x) = (x²+2)/3': phi1,
    'φ2(x) = √(3x-2)': phi2,
    'φ3(x) = 3 - 2/x': phi3,
    'φ4(x) = (x²-2)/(2x-3)': phi4
}

results = {}
for name, phi in methods.items():
    history, errors = iterative_method(phi, x0, iterations)
    results[name] = {'history': history, 'errors': errors}


# Obliczenie rzędów zbieżności
def compute_convergence_order(errors):
    orders = []
    for k in range(1, len(errors) - 1):
        if errors[k] < 1e-15 or errors[k - 1] < 1e-15:
            orders.append(np.nan)
            continue
        try:
            ratio1 = errors[k + 1] / errors[k]
            ratio2 = errors[k] / errors[k - 1]
            if ratio1 < 1e-15 or ratio2 < 1e-15:
                orders.append(np.nan)
                continue
            numerator = np.log(ratio1)
            denominator = np.log(ratio2)
            r = numerator / denominator
            orders.append(r)
        except:
            orders.append(np.nan)
    return orders


# Obliczenie i wyświetlenie rzędów zbieżności
print("\nRzędy zbieżności dla ostatnich iteracji:")
for name, data in results.items():
    orders = compute_convergence_order(data['errors'])

    for i in range(10):
        print(f'iteracja: {i + 1} : x = phi(x) = {data["history"][i]}')

    a = len(orders)

    for i in range(a):
        print(f'k: {i + 2} {name} : {orders[i]}')


# Wykresy błędów dla wszystkich metod
plt.figure(figsize=(12, 8))
for name, data in results.items():
    plt.semilogy(data['errors'], 'o-', label=name)

plt.xlabel('Numer iteracji', fontsize=12)
plt.ylabel('Błąd bezwzględny (skala logarytmiczna)', fontsize=12)
plt.title('Zbieżność metod iteracyjnych', fontsize=14)
plt.legend()
plt.grid(True, which="both", ls="-")
plt.show()

# Wykres dla metod zbieżnych:
plt.figure(figsize=(12, 8))
for name, data in results.items():
    if name != 'φ1(x) = (x²+2)/3':  # Pomijamy metodę rozbieżną
        plt.semilogy(data['errors'], 'o-', label=name)

plt.xlabel('Numer iteracji', fontsize=12)
plt.ylabel('Błąd bezwzględny (skala logarytmiczna)', fontsize=12)
plt.title('Zbieżność metod iteracyjnych (tylko metody zbieżne)', fontsize=14)
plt.legend()
plt.grid(True, which="both", ls="-")
plt.show()