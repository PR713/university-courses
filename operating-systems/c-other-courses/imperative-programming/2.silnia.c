#include <stdio.h>

int main(void) {

    int n, s = 1;
    printf("Podaj n: ");
    scanf_s("%d", &n);
    for (int i = 1; i <= n; i++) {
        s *= i;
    }
    printf("Silnia %d to %d\n", n, s);
    return 0;
}
