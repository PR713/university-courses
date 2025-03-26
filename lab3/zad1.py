import numpy as np
import matplotlib.pyplot as plt

years = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980], dtype=float)
population = np.array([76212168, 92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203302031, 226542199],
                      dtype=float)


def base_0(t):
    return t  # j(t) = t^(j-1)


def base_1(t):
    return t - 1900  # j(t) = (t - 1900)^(j-1)


def base_2(t):
    return t - 1940  # j(t) = (t - 1940)^(j-1)


def base_3(t):
    return (t - 1940) / 40  # j(t) = ((t - 1940) / 40)^(j-1)


base_functions = [base_0, base_1, base_2, base_3]

# Tworzenie macierzy Vandermonde’a dla różnych baz... 1,x,..., x**8
vandermondes = [np.vander(base(years), increasing=True) for base in base_functions]

# Obliczanie współczynnika uwarunkowania dla każdej macierzy
condition_numbers = [np.linalg.cond(V) for V in vandermondes]

# Znalezienie najlepiej uwarunkowanej bazy
best_index = np.argmin(condition_numbers)  # zwraca index
best_phi = base_functions[best_index]
best_vandermonde = vandermondes[best_index]
best_cond = condition_numbers[best_index]

basis_labels = [
    "j(t) = t^(j-1)",
    "j(t) = (t - 1900)^(j-1)",
    "j(t) = (t - 1940)^(j-1)",
    "j(t) = ((t - 1940) / 40)^(j-1)"
]

print("Współczynniki uwarunkowania macierzy Vandermonde’a dla różnych baz:")
for label, cond in zip(basis_labels, condition_numbers):
    print(f"{label}: {cond:.5e}\n")

print(f"Najlepiej uwarunkowana funkcja bazowa: {basis_labels[best_index]} (Współczynnik: {best_cond:.5e})\n")

# Rozwiązanie układu równań w celu znalezienia współczynników wielomianu interpolacyjnego
coefficients = np.linalg.solve(best_vandermonde, population)


def horner(poly_coeffs, x_values):
    """Funkcja implementująca schemat Hornera do szybkiego obliczania wartości wielomianu.
    poly_coeffs - współczynniki wielomianu (od najmniejszego stopnia do najwyższego)
    x_values - wartości x, dla których obliczamy wartości wielomianu"""
    result = np.zeros_like(x_values, dtype=float)
    for i, x in enumerate(x_values):
        value = poly_coeffs[-1]  # Najwyższy współczynnik
        for coef in reversed(poly_coeffs[:-1]): #slice
            value = value * x + coef
        result[i] = value
    return result #lista wartości wielomianu dla każdego punktu


# Definiujemy przedział [1900, 1990] z krokiem 1 rok
x_values = np.arange(1900, 1991, 1)
y_values_horner = horner(coefficients, best_phi(x_values))

# Tworzenie wykresu
plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values_horner, label="Interpolacja Hornera", color='blue')  # Krzywa interpolacyjna
plt.scatter(years, population, color='red', label="Węzły interpolacji", zorder=3)  # Punkty interpolacyjne
plt.xlabel("Rok")
plt.ylabel("Populacja")
plt.title("Wielomian interpolacyjny Hornera populacji USA")
plt.legend()
plt.grid()
plt.show()


def lagrange_interpolation(x, x_data, y_data):
    """Funkcja obliczająca wartość wielomianu interpolacyjnego Lagrange’a w punkcie x.
    x_data - węzły interpolacji (lata)
    y_data - wartości w węzłach (populacja)"""

    n = len(x_data)
    res = 0.0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        res += term

    return res


# Podpunkt (d):
x_extrapolate = 1990
# Aby wywołać funkcję horner dla pojedynczej wartości, przekazujemy tablicę z jednym elementem:
pop_1990 = horner(coefficients, np.array([best_phi(x_extrapolate)]))[0]
#otrzymujemy wartość wielomianu w punkcie x_extrapolate

true_pop_1990 = 248709873
relative_error_1990 = (abs(pop_1990 - true_pop_1990) / true_pop_1990) * 100

print(f"Populacja 1990 (ekstrapolacja): {pop_1990:.2f}")
print(f"Błąd względny ekstrapolacji: {relative_error_1990:.2f}%\n")


y_values_lagrange = np.array([lagrange_interpolation(x, years, population) for x in x_values])

plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values_lagrange, label="Wielomian Lagrange'a", color='blue')
plt.scatter(years, population, color='red', label="Węzły interpolacji", zorder=5)
plt.xlabel("Rok")
plt.ylabel("Populacja")
plt.title("Wielomian interpolacyjny Lagrange'a populacji USA")
plt.legend()
plt.grid()
plt.show()


# f)

def divided_differences(x_data, y_data):
    """
        Funkcja obliczająca ilorazy różnicowe dla wielomianu Newtona.
        x_data - węzły interpolacji (lata)
        y_data - wartości w węzłach (populacja)
        """

    n = len(x_data)
    F = np.zeros((n, n))
    F[:, 0] = y_data
    res = np.zeros(n)
    res[0] = F[0, 0] #f(x0)

    #F[i, j] = f[x_i-j, x_i-j+1, ..., x_i]

    for j in range(1, n):
        for i in range(j, n):
            F[i, j] =  (F[i, j - 1] - F[i - 1, j - 1]) / (x_data[i] - x_data[i-j])
            if i == j:
                res[i] = F[i, j] # f[x0, x1, ... xj]

    return res


def newton_interpolation(x, x_data, coeffs):
    """Funkcja obliczająca wartość wielomianu Newtona w punkcie x.
    x_data - węzły interpolacji (lata)
    coeffs - współczynniki wielomianu Newtona (ilorazy różnicowe)"""

    n = len(coeffs)
    P = coeffs[0]

    for i in range(1, n):
        term = coeffs[i]
        for j in range(i):
            term *= (x - x_data[j])
        P += term

    return P

coeffs = divided_differences(years, population)
y_values_newton = np.array([newton_interpolation(x, years, coeffs) for x in x_values])

plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values_newton, label="Wielomian Newtona", color='green')
plt.scatter(years, population, color='red', label="Węzły interpolacji", zorder=5)
plt.xlabel("Rok")
plt.ylabel("Populacja")
plt.title("Wielomian interpolacyjny Newtona populacji USA")
plt.legend()
plt.grid()
plt.show()




#g)
population_rounded = np.round(population / 1e6).astype(int) * 1e6

vandermondes_rounded = [np.vander(base(years), increasing=True) for base in base_functions]

# condition_numbers_rounded = [np.linalg.cond(V) for V in vandermondes_rounded]
#
# best_index_rounded = np.argmin(condition_numbers_rounded)
# best_phi_rounded = base_functions[best_index_rounded]
# best_vandermonde_rounded = vandermondes_rounded[best_index_rounded]
# best_cond_rounded = condition_numbers_rounded[best_index_rounded]
#
# print(f"Najlepiej uwarunkowana funkcja bazowa z zaokrąglonymi danymi {basis_labels[best_index_rounded]}\n (Współczynnik: {best_cond_rounded:.5e})\n")
#^^^ macierz vandermonda i tak liczymy patrząc na years więc cond nie zmienia się

coefficients_rounded = np.linalg.solve(best_vandermonde, population_rounded)


true_population_1990 = 248709873
pop_rounded_1990 = horner(coefficients_rounded, np.array([best_phi(x_extrapolate)]))[0]
relative_error_rounded_1990 = np.abs((pop_rounded_1990 - true_population_1990) / true_population_1990) * 100


print(f"Populacja 1990 (ekstrapolacja z zaokrągleniem): {pop_rounded_1990:.2f}")
print(f"Błąd względny ekstrapolacji z zaokrągleniem: {relative_error_rounded_1990:.2f}%\n")
print("Współczynniki wielomianu interpolacyjnego bez zaokrąglenia:")
print(coefficients)
print("Współczynniki wielomianu interpolacyjnego z zaokrągleniem:")
print(coefficients_rounded)

y_values_horner_rounded = horner(coefficients_rounded, best_phi(x_values))

plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values_horner_rounded, label="Interpolacja Hornera z zaokrągleniem do miliona", color='blue')  # Krzywa interpolacyjna
plt.scatter(years, population, color='red', label="Węzły interpolacji", zorder=3)  # Punkty interpolacyjne
plt.xlabel("Rok")
plt.ylabel("Populacja")
plt.title("Wielomian interpolacyjny Hornera z zaokrągleniem populacji USA")
plt.legend()
plt.grid()
plt.show()


