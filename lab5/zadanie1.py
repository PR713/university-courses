
import numpy as np
from matplotlib import pyplot as plt

# Dane: lata i odpowiadające im wartości populacji (dane z lat 1900-1980)
years = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980])
populations = np.array([76212168, 92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203302031, 226542199],
                      dtype=float)

t = years - 1900
t_extrap = 1990 - 1900
n = len(t) # 9 punktów
true_1990 = 248709873
t_range = np.linspace(0, 90, 300)
results = []
aicc_values = []

plt.figure(figsize=(12, 7))
colors = plt.cm.viridis(np.linspace(0, 1, 7))

for m in range(7):
    k = m + 1
    coeffs = np.polyfit(t, populations, m)
    poly = np.poly1d(coeffs)

    # Ekstrapolacja dla roku 1990
    pred = poly(t_extrap)
    rel_error = abs(pred - true_1990) / true_1990

    #reszty i błędt średniokwadratowego
    residuals = populations - poly(t)
    rss = np.sum(residuals ** 2)
    mse = rss / n

    # AIC
    AIC = 2 * k + n * np.log(mse)
    # AICc (skorygowany Akaike)
    AICc = AIC + (2 * k * (k + 1)) / (n - k - 1)

    results.append((m, pred, rel_error))
    aicc_values.append((m, AICc))

    plt.plot(t_range, poly(t_range), label=f'm = {m}', color=colors[m])
    plt.scatter([t_extrap], [pred], color=colors[m], marker='x', s=80)


plt.scatter(t, populations, color='black', label='Dane źródłowe', zorder=5)
plt.axvline(x=t_extrap, linestyle='--', color='gray', label='1990 (ekstrapolacja)')
plt.scatter([t_extrap], [true_1990], color='black', marker='o', s=80, label='Prawdziwa wartość 1990')

# Opis wykresu
plt.xlabel('Lata od 1900')
plt.ylabel('Populacja')
plt.title('Aproksymacja populacji USA (1900–1980) wielomianami różnych stopni')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Wyniki podpunktu (a)
print("PODPUNKT (a): Ekstrapolacja na 1990")
print("m \tPredykcja \t\t\tBłąd względny")
for m, pred, rel_error in results:
    print(f"{m} \t{pred:,.2f} \t{rel_error:.4f}")

# Wyniki podpunktu (b)
print("\nPODPUNKT (b): AICc dla każdego stopnia wielomianu")
print("m \tAICc")
for m, aicc in aicc_values:
    print(f"{m} \t{aicc:.2f}")

# Najlepszy model wg AICc
best_m_aicc = min(aicc_values, key=lambda x: x[1])[0]
print(f"\nNajmniejsza wartość AICc dla m = {best_m_aicc}")
