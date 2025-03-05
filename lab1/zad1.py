import numpy as np
import matplotlib.pyplot as plt

# Definicje funkcji
def f(x):
    return np.tan(x)

def f_analytical_prime(x):
    return 1 + np.tan(x)**2  # tożsamość: tan'(x)=1+tan^2(x)

def f_second(x):
    # f''(x)= 2*sec^2(x)*tan(x) = 2*(1/cos^2(x))*tan(x)
    return 2*(1 + np.tan(x)**2)*np.tan(x)

def f_third(x):
    # f'''(x)= 2*sec^2(x) + 6*(sin^2(x))/(cos^4(x))
    return 2*(1 + np.tan(x)**2) + 6*(np.sin(x)**2)/(np.cos(x)**4)

# Punkt, w którym liczymy pochodną
x0 = 1.0
d_true = f_analytical_prime(x0)

# Ustalamy epsilon maszynowy
eps = np.finfo(float).eps

# Generujemy wartości h: h = 10^{-k}, k=0,...,16
k_vals = np.arange(0, 17)
h_vals = 10.0**(-k_vals)

# -------------------------
# RÓŻNICE DO PRZODU (wzór (1))
# -------------------------
d_forward = (f(x0 + h_vals) - f(x0)) / h_vals
error_forward = np.abs(d_forward - d_true)

# Błąd metody (truncation error) ~ (|f''(x0)|/2)*h
E_trunc_forward = 0.5 * np.abs(f_second(x0)) * h_vals
# Szacowany błąd obliczeniowy (roundoff error) ~ 2*eps/h
E_round_forward = 2 * eps / h_vals

# Znajdujemy empiryczne h_min dla metody do przodu
idx_min_forward = np.argmin(error_forward)
h_min_forward_emp = h_vals[idx_min_forward]
E_min_forward_emp = error_forward[idx_min_forward]

# Teoretyczne h_min z wzoru (2): hmin ≈ 2*sqrt(eps/M), gdzie M ≈ |f''(x0)|
M_forward = np.abs(f_second(x0))
h_min_forward_theor = 2 * np.sqrt(eps / M_forward)

# -------------------------
# RÓŻNICE CENTRALNE (wzór (3))
# -------------------------
d_central = (f(x0 + h_vals) - f(x0 - h_vals)) / (2 * h_vals)
error_central = np.abs(d_central - d_true)

# Błąd metody (truncation error) ~ (|f'''(x0)|/6)*h^2
E_trunc_central = (np.abs(f_third(x0)) / 6) * h_vals**2
# Szacowany błąd obliczeniowy (roundoff error) ~ eps/h
E_round_central = eps / h_vals

# Znajdujemy empiryczne h_min dla metody centralnej
idx_min_central = np.argmin(error_central)
h_min_central_emp = h_vals[idx_min_central]
E_min_central_emp = error_central[idx_min_central]

# Teoretyczne h_min z wzoru (4): hmin ≈ (3*eps/M)^(1/3), gdzie M ≈ |f'''(x0)|
M_central = np.abs(f_third(x0))
h_min_central_theor = (3 * eps / M_central)**(1/3)

# -------------------------
# WYKRESY
# -------------------------
plt.figure(figsize=(12, 6))
plt.loglog(h_vals, error_forward, 'o-', label='Błąd numeryczny (różnice do przodu)')
plt.loglog(h_vals, E_trunc_forward, 's--', label='Błąd metody (truncation, do przodu)')
plt.loglog(h_vals, E_round_forward, 'd--', label='Błąd obliczeniowy (roundoff, do przodu)')
plt.axvline(h_min_forward_emp, color='gray', linestyle=':',
            label=f'h_min empiryczne = {h_min_forward_emp:.1e}')
plt.xlabel('h')
plt.ylabel('Błąd')
plt.title('Metoda różnic do przodu')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

plt.figure(figsize=(12, 6))
plt.loglog(h_vals, error_central, 'o-', label='Błąd numeryczny (różnice centralne)')
plt.loglog(h_vals, E_trunc_central, 's--', label='Błąd metody (truncation, centralne)')
plt.loglog(h_vals, E_round_central, 'd--', label='Błąd obliczeniowy (roundoff, centralne)')
plt.axvline(h_min_central_emp, color='gray', linestyle=':',
            label=f'h_min empiryczne = {h_min_central_emp:.1e}')
plt.xlabel('h')
plt.ylabel('Błąd')
plt.title('Metoda różnic centralnych')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

# -------------------------
# WYŚWIETLENIE WYNIKÓW
# -------------------------
print("Dla metody różnic do przodu:")
print(f"  Empiryczne h_min: {h_min_forward_emp:.3e}, E(h_min): {E_min_forward_emp:.3e}")
print(f"  Teoretyczne h_min (wzór (2)): {h_min_forward_theor:.3e}")
print()

print("Dla metody różnic centralnych:")
print(f"  Empiryczne h_min: {h_min_central_emp:.3e}, E(h_min): {E_min_central_emp:.3e}")
print(f"  Teoretyczne h_min (wzór (4)): {h_min_central_theor:.3e}")
print()

if E_min_central_emp < E_min_forward_emp:
    print("Metoda różnic centralnych jest dokładniejsza.")
else:
    print("Metoda różnic do przodu jest dokładniejsza.")
