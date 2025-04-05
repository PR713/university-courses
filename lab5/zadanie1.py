import numpy as np

# Dane: lata i odpowiadające im wartości populacji (dane z lat 1900-1980)
years = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980])
populations = np.array([76212168, 92228496, 106021537, 123202624, 132164569, 151325798, 179323175, 203302031, 226542199],
                      dtype=float)

t = years - 1900
t_extrap = 1990 - 1900
n = len(t) #9 p
true_1990 = 248709873  # Prawdziwa wartość dla roku 1990

results = []
aicc_values = []

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
