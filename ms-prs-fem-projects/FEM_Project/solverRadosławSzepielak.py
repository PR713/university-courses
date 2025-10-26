import numpy as np
import seaborn
from scipy.integrate import quad
import matplotlib.pyplot as plt


class OdksztalceniaSprezyste:
    def __init__(self, n):
        self.n = n

    def calcValueInsideIntegral(self, x, i, j):  # oblicz wartość E(x)*e'*v'
        if x <= 1:
            E = 2
        else:
            E = 6

        if x <= (2 * i - 2) / self.n or x >= (2 * i + 2) / self.n:
            eprim_i = 0
        elif x <= (2 * i) / self.n:
            eprim_i = self.n / 2
        else:
            eprim_i = -self.n / 2

        if x <= (2 * j - 2) / self.n or x >= (2 * j + 2) / self.n:
            eprim_j = 0
        elif x <= (2 * j) / self.n:
            eprim_j = self.n / 2
        else:
            eprim_j = -self.n / 2

        return E * eprim_i * eprim_j

    def calcIntegral(self, i, j):  # oblicz wartość całki za pomocą kwadratury Gaussa
        if abs(j - i) > 1:
            return 0

        start = 2 * max(max(i, j) - 1, 0) / self.n
        end = 2 * min(min(i, j) + 1, self.n) / self.n  # całkowanie od 0 do 2 ale
        # funkcje bazowe ei poza [start,end] liczonymi na bieżąco są równe 0 więc można je pominąć

        if abs(j - i) <= 1:
            # Kwadratura Gaussa-Kronroda obliczająca całkę jako sumę ważoną
            # wartości funkcji w określonych punktach
            return quad(self.calcValueInsideIntegral, start, end, args=(i, j))[0]
        else:
            return 0

    def get_u(self, wMatrixCoefficients):
        def u(x):
            result = 0
            for i in range(self.n):
                result += wMatrixCoefficients[i] * max(0, 1 - abs(x * self.n / 2 - i))
            return result + 3 # + 3 bo u(x) = w(x) + u^(x) = w(x) + 3 (u_bar to u^(x) = 3)

        return u


    def solveAndShowPlot(self):
        e = lambda i, x: max(0, 1 - abs(x * self.n / 2 - i))

        # Definicja funkcji warunku brzegowego
        u_bar = 3

        # Tworzenie macierzy B i wektora L
        B_matrix = np.zeros((self.n, self.n))
        L_matrix = np.zeros(self.n)
        for i in range(self.n):
            for j in range(self.n):
                integral_result = self.calcIntegral(i, j)
                B_matrix[i, j] = integral_result - 2 * e(i, 0) * e(j, 0)

            # uzupełniam macierz L zgodnie z tym co napisałem na kartce
            L_matrix[i] = -14 * e(i, 0) # - 14 * e_i (0)

        # Rozwiązanie macierzy dla w(x)
        w_x = np.linalg.solve(B_matrix, L_matrix)

        # Dodanie warunku brzegowego do w(x)
        u_x = self.get_u(w_x)
        # Tworzenie listy u(x) dla wszystkich punktów x
        u_x_list = [u_x(2 * i / self.n) for i in range(self.n)]
        u_x_list.append(u_bar)


        # Wyświetlanie wykresu
        seaborn.lineplot(x=np.linspace(0, 2, self.n + 1), y=u_x_list)
        #^^^ dzielimy na n przedziałów więc mamy n+1 punktów, n + 1-szy punkt to u_bar = 3, sztywny warunek brzegowy
        #trzeba go dać, inaczej dla małych n się rozjedzie, im większe to tego i tak nie widać
        plt.title(f'Wykres odkształceń sprężystych n = {self.n}' )
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('u(x)')
        plt.show()


def main():
    n = int(input("Podaj n: "))
    model = OdksztalceniaSprezyste(n)
    model.solveAndShowPlot()


if __name__ == '__main__':
    main()
