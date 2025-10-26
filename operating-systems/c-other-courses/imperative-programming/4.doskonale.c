#include <stdio.h>

int main(void) {
    int s = 1, n, cnt = 0;
    printf("Podaj zakres: ");
    scanf_s("%d", &n);
    for (int i = 2; i <= n; i++) {
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                s += j + i / j;
            }
        }
        if (s == i) {
            cnt += 1;
            printf("Doskonala %d\n", i);
        }
    s = 1;

    }
    printf("Liczba doskonalych: %d\n", cnt);
    return 0;
}