//Znajdź pole powierzchni ograniczone osią Ox i wykresem funkcji sin(x) w przedziale
// [a,b] metodą Monte Carlo. Dane wejściowe:a,b,N (liczba losowanych punktów).
//polega na generowaniu losowych punktów i sprawdzaniu, czy znajdują się one nad, pod
//czy na wykresie funkcji sin(x).Liczymy stosunek punktów, które spełniają warunki,
//do całkowitej liczby punktów, a następnie używamy tego stosunku do przybliżonego 
//obliczenia pola powierzchni.

#include <stdio.h>
#include <cmath>
#include <stdlib.h>
#include <time.h>

int main(void) {
	int N;
	float a, b;
	int above_curve = 0, under_curve = 0;
	printf("Podaj przedzial [a,b] i liczbe losowanych punktow: ");
	scanf_s("%f %f %d", &a,&b,&N);
	printf("Wybrany przedzial: [%f,%f], liczba punktow: %d\n", a, b, N);
	srand(time(NULL));

	for (int i = 0; i < N; i++) {

		double x = ((double)rand() / RAND_MAX) * (b - a) + a;//rand_max to max wartość
		//jaką może zwrócić rand() więc będzie ona z przedziału [0,1) bo rand_max zawsze
		// będzie ciut większa od rand()
		double y = ((double)rand() / RAND_MAX) * 2.0 - 1.0; //Zakładamy maksymalną wartość
		//funkcji sin(x) jako 1.0, szerokość przedziału 2.0 a potem cofamy o 1.0

		if (y >= 0 && y <= sin(x)) {
			under_curve++;
		}
		else if (y <= 0 && y >= sin(x)) {
			above_curve++;
		}
	}
	double stosunek = (abs((double)under_curve - (double)above_curve)) / N;
	if ((double)under_curve - (double)above_curve < 0) { // z ujemnym znakiem
		stosunek = -stosunek;
	}

	//stosunek to stosunek liczby punktów które są pod wykresem sinusa lub nad
	// tzn które trafiły w obszar ograniczony sinusem i ox do wszystkich
	double estimated_area = (stosunek) * (b-a) * 2.0;//szerokość przedziału a,b i szerokość y
	printf("%lf",estimated_area);

	return 0;
}