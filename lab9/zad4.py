import numpy as np

# Funkcja definująca równanie y' = f(t,y)
def f(t, y):
    return -5 * y

# (d) Metoda Eulera jawna
def euler_explicit(y0, t0, h, steps):
    y = y0
    t = t0
    for _ in range(steps):
        y = y + h * f(t, y)
        t = t + h
    return y

# (f) Metoda Eulera niejawna
# rozwiązujemy: y_{n+1} = y_n + h * f(t_{n+1}, y_{n+1})
# tutaj f(t, y) = -5 y, więc: y_{n+1} = y_n + h * (-5 y_{n+1})
# => y_{n+1} (1 + 5h) = y_n => y_{n+1} = y_n / (1 + 5h)
def euler_implicit(y0, h, steps):
    y = y0
    for _ in range(steps):
        y = y / (1 + 5 * h)
    return y

# (g) Wyznaczenie maksymalnego kroku h dla zadanej tolerancji (błąd < 0.001)
def find_max_h(y0, t0, t_end, tol):
    # Zrobimy pętlę testując różne h i obliczając y(t_end)
    h = 0.5
    while h > 1e-5:
        steps = int((t_end - t0) / h)
        y_num = euler_explicit(y0, t0, h, steps)
        y_exact = np.exp(-5 * t_end)
        error = abs(y_num - y_exact)
        if error < tol:
            return h, steps, y_num, y_exact, error
        h /= 2
    return None

# (h) Sprawdzenie zbieżności iteracyjnej metody bezpośredniej iteracji (Picarda)
# y_{n+1}^{(k+1)} = y_n + h * f(t_{n+1}, y_{n+1}^{(k)})
# Tutaj f(t,y) = -5 y
def picard_iteration(y_n, h, max_iter=100, tol=1e-10):
    y_new = y_n  # startujemy od y_n
    for _ in range(max_iter):
        y_old = y_new
        y_new = y_n + h * (-5 * y_old)
        if abs(y_new - y_old) < tol:
            return y_new, True
    return y_new, False  # nie zbiega się

def test_picard_convergence(y0, h):
    converged, iteration_count = False, 0
    y_n = y0
    y_guess = y_n
    for _ in range(10):
        y_new, converged = picard_iteration(y_n, h)
        iteration_count += 1
        if not converged:
            break
        y_n = y_new
    return converged

if __name__ == "__main__":
    y0 = 1
    t0 = 0
    t_end = 0.5
    h = 0.5
    steps = int((t_end - t0) / h)

    # (d)
    y_explicit = euler_explicit(y0, t0, h, steps)
    y_exact = np.exp(-5 * t_end)
    print(f"(d) Euler jawny, y({t_end}) = {y_explicit:.6f}, rozwiązanie analityczne = {y_exact:.6f}")

    # (f)
    y_implicit = euler_implicit(y0, h, steps)
    print(f"(f) Euler niejawny, y({t_end}) = {y_implicit:.6f}")

    # (g)
    tol = 0.001
    result = find_max_h(y0, t0, t_end, tol)
    if result:
        max_h, steps_needed, y_num, y_exact, error = result
        print(f"(g) Maksymalny krok h = {max_h:.6f}, liczba kroków = {steps_needed}")
        print(f"    y_num = {y_num:.6f}, y_exact = {y_exact:.6f}, błąd = {error:.6f}")
    else:
        print("(g) Nie znaleziono kroku spełniającego tolerancję")

    # (h)
    print(f"(h) Sprawdzenie zbieżności metody Picarda dla h = {h}")
    converged = test_picard_convergence(y0, h)
    print(f"    Zbieżność iteracji Picarda: {'TAK' if converged else 'NIE'}")
    print("    Użycie metody Newtona byłoby uzasadnione, gdy iteracje Picarda nie zbiegałyby szybko.")
