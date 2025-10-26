//Program losuje liczbę 0≤X≤100. Napisz funkcję, która zgaduje wartośćX.
// W pętli losujemy n∈[0, 100]. Jeżeli X = n zgadliśmy X, jeżeli nie na podstawie
// wartości X i n ograniczamy przedział, z którego losujemy kolejne n.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>

int losowanie(int x) {
	int i = 101, start = 0, end = 100; // i szerokość, start - początek, end - koniec
	Sleep(2000); // end i start moga być też ujemne dowolone :) ale wtedy i = abs
	srand(time(NULL));
	while (1) {
		
		int n = (rand() % i) + start; // od start...end potem zawężamy
		printf("N to %d", n);
		if (n == x) {
			printf("\nZgadles! x = %d\n", n);
			break;
		}
		else if (n < x) {
			start = n + 1;
			i = end - start + 1;
		}
		else { // n > x
			end = n - 1;
			i = end - start + 1;
		}
		printf(" a przedzial to <%d,%d>\n", start, end);
	}
	return x;
}


int main() {

	srand(time(NULL));
	int x = rand() % 101; // od 0...100 reszta
	printf("Wylosowano %d a przedzial <0,100>\n", x);
	return losowanie(x);
}