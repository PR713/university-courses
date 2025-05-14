import numpy as np


def F(x):
    x1, x2 = x
    return np.array([
        x1 ** 2 + x2 ** 2 - 1,
        x1 ** 2 - x2
    ])


def J(x):
    x1, x2 = x
    return np.array([
        [2 * x1, 2 * x2],
        [2 * x1, -1]
    ])


def newton_system(F, J, x0, tol=1e-14, max_iter=6):
    x = x0
    for _ in range(max_iter):
        Fx = F(x)
        Jx = J(x)
        delta = np.linalg.solve(Jx, -Fx)
        x = x + delta
        if np.linalg.norm(delta, ord=2) < tol:
            break
    return x


# Punkt startowy
x0 = np.array([0.5, 1.5])
approx_solution = newton_system(F, J, x0)

# Dokładne rozwiązania
x2_exact = np.sqrt(5) / 2 - 0.5
x1_exact = np.sqrt(x2_exact)
exact_solution = np.array([x1_exact, x2_exact])

relative_error1 = abs(exact_solution[0] - approx_solution[0]) / approx_solution[0]
relative_error2 = abs(exact_solution[1] - approx_solution[1]) / approx_solution[1]

np.set_printoptions(precision=16, suppress=False)

print("Przybliżone rozwiązanie metodą Newtona:", approx_solution)
print("Dokładne rozwiązanie:", exact_solution)
print("Błąd względny 1:", relative_error1)
print("Błąd względny 2:", relative_error2)
