#include <stdio.h>

int main(void) {
    int a = 0, b = 1, c, n;
    printf("Podaj n: ");
    scanf_s("%d", &n);

    while (b < n) {
        c = a + b;
        a = b;
        b = c;
        if (a * b == n) {
            printf("Tak\n");
            return 0;
        }
    }
    printf("Nie\n");
    return 0;
}