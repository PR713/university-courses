#include <stdio.h>
#include <math.h>

double taylor_cos(double x) {
    double result = 1; // Pierwszy składnik to 1
    double term = 1;

    for (int i = 1; i <= 5; i++) {
        term *= x * x / ((2 * i) * (2 * i - 1));
        result += (i % 2 == 0) ? term : -term; //znak przy kolejnych składnikach
    }

    return result;
}

int main() {
    double start, end, krok;

    printf("Podaj poczatek przedzialu: ");
    scanf_s("%lf", &start);
    printf("Podaj koniec przedzialu: ");
    scanf_s("%lf", &end);
    printf("Podaj krok: ");
    scanf_s("%lf", &krok);

    printf("%-15s%-15s%-15s\n", "Wartość x", "cos(x) (bibl.)", "cos(x) (Taylor)");

    double x;
    for (x = start; x <= end; x += krok) {
        printf("%-15lf%-15lf%-15lf\n", x, cos(x), taylor_cos(x));
    }

    return 0;
}