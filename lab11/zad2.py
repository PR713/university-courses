import numpy as np
import matplotlib.pyplot as plt
import random


class RobotPathOptimizer:
    def __init__(self, n, k, start_point, end_point, obstacles, lambda1=1, lambda2=1, epsilon=1e-13):
        """
        Inicjalizacja optymalizatora ścieżki robota
        """
        self.n = n
        self.k = k
        self.start_point = np.array(start_point)
        self.end_point = np.array(end_point)
        self.obstacles = np.array(obstacles)
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.epsilon = epsilon

    def objective_function(self, X):
        """
        Oblicza wartość funkcji celu F(X)
        """
        obstacle_term = 0
        for i in range(self.n + 1):
            for j in range(self.k):
                distance_sq = np.sum((X[i] - self.obstacles[j]) ** 2)
                obstacle_term += 1 / (self.epsilon + distance_sq)

        path_length_term = 0
        for i in range(self.n):
            path_length_term += np.sum((X[i + 1] - X[i]) ** 2)

        return self.lambda1 * obstacle_term + self.lambda2 * path_length_term

    def compute_gradient(self, X):
        gradient = np.zeros_like(X)

        for i in range(self.n + 1):
            for j in range(self.k):
                diff = X[i] - self.obstacles[j]
                distance_sq = np.sum(diff ** 2)
                gradient[i] += -2 * self.lambda1 * diff / (self.epsilon + distance_sq) ** 2

        for i in range(self.n):
            gradient[i] += 2 * self.lambda2 * (X[i] - X[i + 1])
            gradient[i + 1] += 2 * self.lambda2 * (X[i + 1] - X[i])

        gradient[0] = np.zeros(2)
        gradient[self.n] = np.zeros(2)

        return gradient

    def golden_section_search(self, X, direction, alpha_min=0, alpha_max=1, tol=1e-6):
        """
        Implementacja metody złotego podziału dla przeszukiwania liniowego
        """
        phi = (1 + np.sqrt(5)) / 2
        resphi = 2 - phi

        alpha_max = 1.0
        while self.objective_function(X - alpha_max * direction) > self.objective_function(X):
            alpha_max *= 2
            if alpha_max > 100:
                break

        tol1 = tol * (alpha_max - alpha_min)
        alpha1 = alpha_min + resphi * (alpha_max - alpha_min)
        alpha2 = alpha_max - resphi * (alpha_max - alpha_min)

        f1 = self.objective_function(X - alpha1 * direction)
        f2 = self.objective_function(X - alpha2 * direction)

        while abs(alpha_max - alpha_min) > tol1:
            if f1 < f2:
                alpha_max = alpha2
                alpha2 = alpha1
                f2 = f1
                alpha1 = alpha_min + resphi * (alpha_max - alpha_min)
                f1 = self.objective_function(X - alpha1 * direction)
            else:
                alpha_min = alpha1
                alpha1 = alpha2
                f1 = f2
                alpha2 = alpha_max - resphi * (alpha_max - alpha_min)
                f2 = self.objective_function(X - alpha2 * direction)

        return (alpha_min + alpha_max) / 2

    def steepest_descent(self, max_iterations=400, tolerance=1e-8):
        """
        Algorytm największego spadku z przeszukiwaniem liniowym
        """
        X = np.zeros((self.n + 1, 2))
        X[0] = self.start_point
        X[self.n] = self.end_point

        for i in range(1, self.n):
            X[i] = np.random.uniform(0, 20, 2)

        objective_history = []
        gradient_norms = []

        print(f"Iteracja 0: F = {self.objective_function(X):.6f}")

        for iteration in range(max_iterations):
            gradient = self.compute_gradient(X)
            gradient_norm = np.linalg.norm(gradient)

            current_objective = self.objective_function(X)
            objective_history.append(current_objective)
            gradient_norms.append(gradient_norm)

            if gradient_norm < tolerance:
                print(f"Konwergencja osiągnięta w iteracji {iteration}")
                break

            alpha = self.golden_section_search(X, gradient)

            X_new = X - alpha * gradient
            X_new[0] = self.start_point
            X_new[self.n] = self.end_point

            X = X_new

            if (iteration + 1) % 50 == 0:
                print(f"Iteracja {iteration + 1}: F = {current_objective:.6f}, ||∇F|| = {gradient_norm:.6f}")

        return {
            'optimal_path': X,
            'final_objective': self.objective_function(X),
            'objective_history': objective_history,
            'gradient_norms': gradient_norms,
            'iterations': len(objective_history)
        }


def run_experiment():
    np.random.seed(42)
    random.seed(42)

    n = 20
    k = 50
    start_point = [0, 0]
    end_point = [20, 20]
    lambda1 = lambda2 = 1
    epsilon = 1e-13
    max_iterations = 400

    obstacles = np.random.uniform(0, 20, (k, 2))

    print("=== OPTYMALIZACJA ŚCIEŻKI ROBOTA ===")
    print(f"Parametry: n={n}, k={k}, λ₁={lambda1}, λ₂={lambda2}, ε={epsilon}")
    print(f"Start: {start_point}, Koniec: {end_point}")
    print(f"Liczba przeszkód: {k}")
    print("-" * 50)

    results = []

    for trial in range(5):
        print(f"\n--- PRÓBA {trial + 1} ---")
        np.random.seed(42 + trial)

        optimizer = RobotPathOptimizer(n, k, start_point, end_point, obstacles,
                                       lambda1, lambda2, epsilon)
        result = optimizer.steepest_descent(max_iterations)
        results.append(result)

        print(f"Końcowa wartość funkcji celu: {result['final_objective']:.6f}")
        print(f"Liczba iteracji: {result['iterations']}")

    best_trial = 0
    best_obj = float('inf')
    for i, result in enumerate(results):
        if result['final_objective'] < best_obj:
            best_obj = result['final_objective']
            best_trial = i
    best_result = results[best_trial]

    print(f"\n=== NAJLEPSZY WYNIK (Próba {best_trial + 1}) ===")
    print(f"Końcowa wartość funkcji celu: {best_result['final_objective']:.6f}")
    print(f"Liczba iteracji: {best_result['iterations']}")

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

    ax1.scatter(obstacles[:, 0], obstacles[:, 1], c='red', s=30, alpha=0.6, label='Przeszkody')
    ax1.plot(best_result['optimal_path'][:, 0], best_result['optimal_path'][:, 1],
             'b-o', linewidth=2, markersize=4, label='Optymalna ścieżka')
    ax1.plot(start_point[0], start_point[1], 'go', markersize=10, label='Start')
    ax1.plot(end_point[0], end_point[1], 'ro', markersize=10, label='Koniec')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('Optymalna ścieżka robota')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-2, 22)
    ax1.set_ylim(-2, 22)

    ax2.plot(best_result['objective_history'], 'b-', linewidth=2)
    ax2.set_xlabel('Iteracja')
    ax2.set_ylabel('Wartość funkcji celu F')
    ax2.set_title('Zbieżność algorytmu')
    ax2.grid(True, alpha=0.3)
    ax2.set_yscale('log')

    ax3.plot(best_result['gradient_norms'], 'r-', linewidth=2)
    ax3.set_xlabel('Iteracja')
    ax3.set_ylabel('||∇F||')
    ax3.set_title('Norma gradientu')
    ax3.grid(True, alpha=0.3)
    ax3.set_yscale('log')

    for i, result in enumerate(results):
        ax4.plot(result['objective_history'], alpha=0.7, label=f'Próba {i + 1}')
    ax4.set_xlabel('Iteracja')
    ax4.set_ylabel('Wartość funkcji celu F')
    ax4.set_title('Porównanie wszystkich prób')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_yscale('log')

    plt.tight_layout()
    plt.show()

    print("\n=== ANALIZA WYNIKÓW ===")
    final_objectives = [r['final_objective'] for r in results]
    iterations_count = [r['iterations'] for r in results]

    print(f"Średnia wartość funkcji celu: {np.mean(final_objectives):.6f} ± {np.std(final_objectives):.6f}")
    print(f"Najlepsza wartość: {np.min(final_objectives):.6f}")
    print(f"Najgorsza wartość: {np.max(final_objectives):.6f}")
    print(f"Średnia liczba iteracji: {np.mean(iterations_count):.1f} ± {np.std(iterations_count):.1f}")

    path_length = 0
    for i in range(n):
        path_length += np.linalg.norm(best_result['optimal_path'][i + 1] - best_result['optimal_path'][i])

    print(f"Długość optymalnej ścieżki: {path_length:.3f}")

    min_distance_to_obstacle = float('inf')
    for point in best_result['optimal_path']:
        for obstacle in obstacles:
            distance = np.linalg.norm(point - obstacle)
            min_distance_to_obstacle = min(min_distance_to_obstacle, distance)

    print(f"Minimalna odległość od przeszkody: {min_distance_to_obstacle:.3f}")

    return results, obstacles


if __name__ == "__main__":
    results, obstacles = run_experiment()