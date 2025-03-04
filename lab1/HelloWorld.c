#include <stdio.h>

int main() {
    printf("Hello World \n");

    int x, y;

    scanf("Podaj pierwsza liczbe calkowita: %d", &x);
    scanf("Podaj druga liczbe calkowita: %d", &y);
    printf("%d * %d = %d", x, y, x * y);

    return 0;
}