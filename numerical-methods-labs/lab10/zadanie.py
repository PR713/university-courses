
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.integrate import solve_ivp

# Parametry modelu i warunki początkowe
params_default = [1.0, 0.1, 0.5, 0.02]  # alpha1, beta1, alpha2, beta2
x0, y0 = 20.0, 20.0
T = 80
h = 0.1
t_points = np.arange(0, T + h, h)

# Funkcje modelu
def lotka_volterra(t, z, alpha1, beta1, alpha2, beta2):
    x, y = z
    dxdt = x * (alpha1 - beta1 * y)
    dydt = y * (-alpha2 + beta2 * x)
    return [dxdt, dydt]

# Metoda jawna Eulera
def explicit_euler(f, t_points, y0):
    y = np.zeros((len(t_points), len(y0)))
    y[0] = y0
    for i in range(len(t_points) - 1):
        h = t_points[i+1] - t_points[i]
        y[i+1] = y[i] + h * np.array(f(t_points[i], y[i]))
    return y

# Metoda niejawna Eulera (rozwiązujemy równanie nieliniowe w każdym kroku)
def implicit_euler(f, t_points, y0):
    y = np.zeros((len(t_points), len(y0)))
    y[0] = y0
    for i in range(len(t_points) - 1):
        h = t_points[i+1] - t_points[i]
        def equation(y_next):
            return y_next - y[i] - h * np.array(f(t_points[i+1], y_next))
        y[i+1] = minimize(lambda yn: np.sum(equation(yn)**2), y[i]).x
    return y

# Półjawna metoda Eulera (dla x jawna, dla y niejawna)
def semi_implicit_euler(t_points, y0, alpha1, beta1, alpha2, beta2):
    y = np.zeros((len(t_points), 2))
    y[0] = y0
    for i in range(len(t_points) - 1):
        h = t_points[i+1] - t_points[i]
        x_prev, y_prev = y[i]
        # Najpierw y_{n+1} (niejawnie)
        y_next = y_prev / (1 + h * (alpha2 - beta2 * x_prev))
        # Potem x_{n+1} (jawnie)
        x_next = x_prev + h * x_prev * (alpha1 - beta1 * y_next)
        y[i+1] = [x_next, y_next]
    return y

def rk4(f, t_points, y0):
    y = np.zeros((len(t_points), len(y0)))
    y[0] = y0
    for i in range(len(t_points) - 1):
        h = t_points[i+1] - t_points[i]
        t = t_points[i]
        k1 = np.array(f(t, y[i]))
        k2 = np.array(f(t + h/2, y[i] + h/2 * k1))
        k3 = np.array(f(t + h/2, y[i] + h/2 * k2))
        k4 = np.array(f(t + h, y[i] + h * k3))
        y[i+1] = y[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
    return y


# Rozwiązania
alpha1, beta1, alpha2, beta2 = params_default
lv_func = lambda t, z: lotka_volterra(t, z, alpha1, beta1, alpha2, beta2)
sol_explicit = explicit_euler(lv_func, t_points, [x0, y0])
sol_implicit = implicit_euler(lv_func, t_points, [x0, y0])
sol_semi_implicit = semi_implicit_euler(t_points, [x0, y0], alpha1, beta1, alpha2, beta2)
sol_rk4 = rk4(lv_func, t_points, [x0, y0])
sol_ref = solve_ivp(lambda t, z: lotka_volterra(t, z, alpha1, beta1, alpha2, beta2), [0, T], [x0, y0], t_eval=t_points, method='LSODA')


# Wykresy
def plot_population_separate():
    plt.figure(figsize=(20, 10))

    # Wykres dla ofiar
    plt.subplot(2, 1, 1)
    methods = [(sol_explicit, 'Euler jawny', '-'), (sol_implicit, 'Euler niejawny', '--'),
               (sol_semi_implicit, 'Euler półjawny', '-.'), (sol_rk4, 'RK4', ':'),
               ((sol_ref.y[0], sol_ref.y[1]), 'Referencyjny', 'k')]
    for sol, label, style in methods:
        if isinstance(sol, tuple):
            plt.plot(t_points, sol[0], style, label=f'Ofiary ({label})')
        else:
            plt.plot(t_points, sol[:, 0], style, label=f'Ofiary ({label})')
    plt.xlabel('Czas')
    plt.ylabel('Populacja ofiar')
    plt.title('Populacja ofiar w czasie')
    plt.legend()
    plt.grid()

    # Wykres dla drapieżników
    plt.subplot(2, 1, 2)
    for sol, label, style in methods:
        if isinstance(sol, tuple):
            plt.plot(t_points, sol[1], style, label=f'Drapieżniki ({label})')
        else:
            plt.plot(t_points, sol[:, 1], style, label=f'Drapieżniki ({label})')
    plt.xlabel('Czas')
    plt.ylabel('Populacja drapieżników')
    plt.title('Populacja drapieżników w czasie')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


def plot_phase():
    plt.figure(figsize=(8, 8))
    plt.plot(sol_explicit[:, 0], sol_explicit[:, 1], label='Euler jawny')
    plt.plot(sol_implicit[:, 0], sol_implicit[:, 1], '--', label='Euler niejawny')
    plt.plot(sol_semi_implicit[:, 0], sol_semi_implicit[:, 1], '-.', label='Euler półjawny')
    plt.plot(sol_rk4[:, 0], sol_rk4[:, 1], ':', label='RK4')
    plt.plot(sol_ref.y[0], sol_ref.y[1], 'k-', alpha=0.3, linewidth=3, label='Referencyjne')
    plt.xlabel('Ofiary (x)')
    plt.ylabel('Drapieżniki (y)')
    plt.title('Portret fazowy')
    plt.legend()
    plt.grid()
    plt.show()

plot_population_separate()
plot_phase()

print("Punkty stacjonarne:")
print(f"1. (x, y) = (0, 0)")
print(f"2. (x, y) = ({alpha2 / beta2}, {alpha1 / beta1})")


# Funkcja niezmiennika
def hamiltonian(x, y):
    return beta2 * x + beta1 * y - alpha2 * np.log(x) - alpha1 * np.log(y)

def plot_hamiltonians():
    H = lambda sol: [hamiltonian(x, y) for x, y in sol]
    H_ref = [hamiltonian(x, y) for x, y in zip(sol_ref.y[0], sol_ref.y[1])]
    plt.figure(figsize=(12, 6))
    plt.plot(t_points, H(sol_explicit), label='Euler jawny')
    plt.plot(t_points, H(sol_implicit), '--', label='Euler niejawny')
    plt.plot(t_points, H(sol_semi_implicit), '-.', label='Euler półjawny')
    plt.plot(t_points, H(sol_rk4), ':', label='RK4')
    plt.plot(t_points, H_ref, 'k-', alpha=0.3, linewidth=3, label='Referencyjne')
    plt.xlabel('Czas')
    plt.ylabel('H(x, y)')
    plt.title('Niezmiennik H(x, y) w czasie')
    plt.legend()
    plt.grid()
    plt.show()

plot_hamiltonians()

# Estymacja parametrów
data = np.loadtxt('LynxHare.txt')
years = data[:, 0]
hares = data[:, 1] / np.max(data[:, 1]) * 100
lynxes = data[:, 2] / np.max(data[:, 2]) * 20

def solve_lotka(params, t_points, y0):
    a1, b1, a2, b2 = params
    sol = solve_ivp(lambda t, z: lotka_volterra(t, z, a1, b1, a2, b2),
                    [t_points[0], t_points[-1]], y0, t_eval=t_points, method='LSODA')
    return sol.y[0], sol.y[1]

def cost_rss(params):
    x_pred, y_pred = solve_lotka(params, years - years[0], [hares[0], lynxes[0]])
    return np.sum((hares - x_pred)**2 + (lynxes - y_pred)**2)

def cost_log(params):
    x_pred, y_pred = solve_lotka(params, years - years[0], [hares[0], lynxes[0]])
    return -np.sum(hares * np.log(x_pred + 1e-10) + lynxes * np.log(y_pred + 1e-10)) + np.sum(x_pred + y_pred)

result_rss = minimize(cost_rss, params_default, method='Nelder-Mead')
result_log = minimize(cost_log, params_default, method='Nelder-Mead')

print("\nOptymalne parametry (RSS):", result_rss.x)
print("Optymalne parametry (Log-likelihood):", result_log.x)

x_rss, y_rss = solve_lotka(result_rss.x, years - years[0], [hares[0], lynxes[0]])
x_log, y_log = solve_lotka(result_log.x, years - years[0], [hares[0], lynxes[0]])

plt.figure(figsize=(12, 6))
plt.plot(years, hares, 'b-', label='Dane - zające')
plt.plot(years, lynxes, 'r-', label='Dane - rysie')
plt.plot(years, x_rss, 'b--', label='Model (RSS) - zające')
plt.plot(years, y_rss, 'r--', label='Model (RSS) - rysie')
plt.plot(years, x_log, 'b:', label='Model (Log) - zające')
plt.plot(years, y_log, 'r:', label='Model (Log) - rysie')
plt.xlabel('Rok')
plt.ylabel('Populacja (znormalizowana)')
plt.title('Dopasowanie modelu Lotki-Volterry')
plt.legend()
plt.grid()
plt.show()
