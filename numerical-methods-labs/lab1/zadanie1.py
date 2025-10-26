import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.tan(x)

def f_analytical_prime(x):
    return 1 + np.tan(x)**2  # tożsamość: tan'(x)=1+tan^2(x)

def f_second(x):
    return 2*(1/np.cos(x)**2)*np.tan(x)

def f_third(x):
    return 2*(1/np.cos(x)**2) + 6*(np.sin(x)**2)/(np.cos(x)**4)

x0 = 1.0
d_true = f_analytical_prime(x0)

eps = np.finfo(float).eps

k_vals = np.arange(0, 17)
h_vals = 10.0**(-k_vals)

d_forward = (f(x0 + h_vals) - f(x0)) / h_vals
error_forward = np.abs(d_forward - d_true)

E_trunc_forward = 0.5 * np.abs(f_second(x0)) * h_vals

E_round_forward = 2 * eps / h_vals

idx_min_forward = np.argmin(error_forward)
h_min_forward_emp = h_vals[idx_min_forward]
E_min_forward_emp = error_forward[idx_min_forward]

M_forward = np.abs(f_second(x0))
h_min_forward_theor = 2 * np.sqrt(eps / M_forward)

d_central = (f(x0 + h_vals) - f(x0 - h_vals)) / (2 * h_vals)
error_central = np.abs(d_central - d_true)

E_trunc_central = (np.abs(f_third(x0)) / 6) * h_vals**2

E_round_central = eps / h_vals

idx_min_central = np.argmin(error_central)
h_min_central_emp = h_vals[idx_min_central]
E_min_central_emp = error_central[idx_min_central]

M_central = np.abs(f_third(x0))
h_min_central_theor = (3 * eps / M_central)**(1/3)

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
