//Dana jest liczba całkowita dodatnia n. Napisz program, który znajduje
// wszystkie liczby pierwsze mniejsze od n, których cyfry tworzą ciąg niemalejący.

#include <stdio.h>

int main(void) {
	int n, j, x, a;
	int prevcyfra, currcyfra;
	printf("Podaj liczbe: ");
	scanf_s("%d", &n);

	for (int i = 2; i < n; i++) {
		j = 2;
		x = 1;

		while (j * j <= i) {
			if (i % j == 0) {
				x = 0;
				break;
			}
			j += 1;
		}

		if (x == 1) { // cyfry tworzą ciąg niemalejący
			a = i;// czyli od końca nierosnący np 1222345
			prevcyfra = a % 10;
			a /= 10;
			while (a > 0) {
				currcyfra = a % 10;
				if (currcyfra <= prevcyfra) {
					a /= 10;
					prevcyfra = currcyfra;

				}
				else {
					break;
				}
			}
			if (a == 0) {
				printf("Liczba liczba pierwsza o niemalejacych cyfrach: %d\n", i);
			}
		}
	}
	return 0;
}


	