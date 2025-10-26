#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

#define SIZE 40

void read_vector(double x[], int n) {
	for(int i = 0; i < n; ++i) {
		scanf("%lf", x++);
	}
}

void print_vector(double x[], int n) {
	for(int i = 0; i < n; ++i) {
		printf("%.4f ", x[i]);
	}
	printf("\n");
}

void read_mat(double A[][SIZE], int m, int n) {
	for(int i = 0; i < m; ++i) {
		for(int j = 0; j < n; ++j) {
			scanf("%lf", &A[i][j]);
		}
	}
}

void print_mat(double A[][SIZE], int m, int n) {
	for(int i = 0; i < m; ++i) {
		for(int j = 0; j < n; ++j) {
			printf("%.4f ", A[i][j]);
		}
		printf("\n");
	}
}

// 1. Calculate matrix product, AB = A X B
// A[m][p], B[p][n], AB[m][n]
void mat_product(double A[][SIZE], double B[][SIZE], double AB[][SIZE], int m, int p, int n) {
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++) {
			AB[i][j] = 0; // Wyzerowanie wartości
		}
	}
	for (int i = 0; i < m; i++) { //wiersze A
		for (int x = 0; x < n; x++) { //kolumny B
			for (int j = 0; j < p; j++) { //kolumny A i wiersze B
				AB[i][x] += A[i][j] * B[j][x];
			}
		}
	}
}


// 2. Matrix triangulation and determinant calculation - simplified version
// (no rows' swaps). If A[i][i] == 0, function returns NAN.
// Function may change A matrix elements.
double gauss_simplified(double A[][SIZE], int n) {
	for (int i = 0; i < n; i++) { // kolumny
		if (A[i][i] == 0) {
			return NAN;
		}

		for (int j = i + 1; j < n; j++) {//w danej kolumnie elementy pod przekątną główną
			double x = A[j][i] / A[i][i];
			for (int k = i; k < n; k++) {//można k = 0 ale już będą wyzerowane wcześniejsze el. w tym
				//wierszu j-tym więc A[j][i] będzie równe 0 => x = 0, lepiej k = 1
				A[j][k] -= A[i][k] * x; //k kolejne kolumny w wierszu j-tym, odejmujemy od wiersza j elementy
				//odpowiadające im z wiersza i-tego pomnożone przez x
			}
		}
	}
	double det = 1;
	for (int i = 0; i < n; i++) {
		det *= A[i][i];
	}//simplified Gauss bo nie dopuszczamy na razie zamiany wierszy więc gdy się wyzeruje A[i][i] to :(
	return det;
}

// 3. Matrix triangulation, determinant calculation, and Ax = b solving - extended version
// (Swap the rows so that the row with the largest, leftmost nonzero entry is on top. While
// swapping the rows use index vector - do not copy entire rows.)
// If max A[i][i] < eps, function returns 0.
// If det != 0 && b != NULL && x != NULL then vector x should contain solution of Ax = b.

double gauss(double A[][SIZE], double b[], double x[], const int n, const double eps) {
	int indices[SIZE];//na kolejnych indeksach ma informację o tym z jakim wierszem został zamieniony
	//aby nie zamieniac elementów tylko zostawić A bez zmian z kolejnością wierszy
	double det = 1;

	for (int i = 0; i < n; i++) {
		indices[i] = i;
	}
	
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (fabs(A[indices[i]][i]) < fabs(A[indices[j]][i])) {
				int c = indices[i];
				indices[i] = indices[j];
				indices[j] = c;
				det *= -1;//zamiana wierszy zamienia det(A) na -det(A)
			}
		}
		if (A[indices[i]][i] == 0)
			return 0;

		for (int j = i + 1; j < n; j++) {//to
			double scalar = A[indices[j]][i] / A[indices[i]][i];
			for (int k = i; k < n; k++) {
				A[indices[j]][k] -= A[indices[i]][k] * scalar;
			}
			b[indices[j]] -= b[indices[i]] * scalar;//to samo co w simplified Gauss
		}
	}


	for (int i = 0; i < n; i++) {
		det *= A[indices[i]][i];
	}

	if (det != 0) {//czyli r(A) = n bo istnieje macierz trójkątna
		for (int i = n - 1; i >= 0; i--) {
			double sum = b[indices[i]];
			for (int j = n - 1; j > i; j--) {
				sum -= x[j] * A[indices[i]][j];
			}
			x[i] = sum / A[indices[i]][i];
		}
	}

	return det;
}

// 4. Returns the determinant; B contains the inverse of A (if det(A) != 0)
// If max A[i][i] < eps, function returns 0.
double matrix_inv(double A[][SIZE], double B[][SIZE], int n, double eps) {
	int indices[SIZE];
	double mat_unit[SIZE][SIZE] = { 0 };
	double det = 1;

	for (int i = 0; i < n; i++) {
		indices[i] = i;
	}
	for (int i = 0; i < n; i++) {
		mat_unit[i][i] = 1;
	}

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (fabs(A[indices[i]][i]) < fabs(A[indices[j]][i])) {
				int c = indices[i];
				indices[i] = indices[j];
				indices[j] = c;
				det *= -1;
			}
		}

		if (A[indices[i]][i] == 0)
			return 0;

		for (int j = i + 1; j < n; j++) {
			double scalar = A[indices[j]][i] / A[indices[i]][i];
			for (int k = i; k < n; k++) {
				A[indices[j]][k] -= A[indices[i]][k] * scalar;
			}
			for (int k = 0; k < n; k++) {
				mat_unit[indices[j]][k] -= mat_unit[indices[i]][k] * scalar;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		det *= A[indices[i]][i];
	}


	for (int i = 0; i < n; i++) {//teraz z przekątnej głównej robimy jedynki
		double scalar = A[indices[i]][i];
		for (int j = i; j < n; j++) {
			A[indices[i]][j] /= scalar;

		}
		for (int j = 0; j < n; j++) {
			mat_unit[indices[i]][j] /= scalar;
		}
	}

	for (int i = n - 1; i >= 0; i--) {//teraz trójkątną dolną
		for (int j = i - 1; j >= 0; j--) {
			double scalar = A[indices[j]][i] / A[indices[i]][i];
			for (int k = i; k < n; k++) {
				A[indices[j]][k] -= A[indices[i]][k] * scalar;
			}
			for (int k = 0; k < n; k++) {
				mat_unit[indices[j]][k] -= mat_unit[indices[i]][k] * scalar;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			B[i][j] = mat_unit[indices[i]][j];
		}
	}

	return det;
}

int main(void) {

	double A[SIZE][SIZE], B[SIZE][SIZE], C[SIZE][SIZE];
	double b[SIZE], x[SIZE], det, eps = 1.e-13;

	int to_do;
	int m, n, p;

	scanf ("%d", &to_do);

	switch (to_do) {
		case 1:
			scanf("%d %d %d", &m, &p, &n);
			read_mat(A, m, p);
			read_mat(B, p, n);
			mat_product(A, B, C, m, p, n);
			print_mat(C, m, n);
			break;
		case 2:
			scanf("%d", &n);
			read_mat(A, n, n);
			printf("%.4f\n", gauss_simplified(A, n));
			break;
		case 3:
			scanf("%d", &n);
			read_mat(A,n, n);
			read_vector(b, n);
			det = gauss(A, b, x, n, eps);
			printf("%.4f\n", det);
			if (det) print_vector(x, n);
			break;
		case 4:
			scanf("%d", &n);
			read_mat(A, n, n);
			det = matrix_inv(A, B, n, eps);
			printf("%.4f\n", det);
			if (det) print_mat(B, n, n);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	return 0;
}

