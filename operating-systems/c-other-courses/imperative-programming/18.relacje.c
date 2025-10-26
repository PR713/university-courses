#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_REL_SIZE 100
#define MAX_RANGE 100

typedef struct {
	int first;
	int second;
} pair;

// Add pair to existing relation if not already there
int add_relation(pair* tab, int n, pair new_pair) {
	int i, check = 1;
	for (i = 0; i < n; i++) {
		if (tab[i].first == new_pair.first && tab[i].second == new_pair.second) {
			check = 0;
			break;
		}
	}
	if (!check) return n;
	tab[n] = new_pair;
	return n + 1;
}

// Read number of pairs, n, and then n pairs of ints
int read_relation(pair* relation) { //tworzymy relację
	int number, curr = 0;
	pair tmp;
	scanf("%d", &number);
	for (int i = 0; i < number; i++) {
		scanf("%d %d", &tmp.first, &tmp.second);
		curr = add_relation(relation, curr, tmp);
	}
	return curr;
}

void print_int_array(int* array, int n) {
	printf("%d\n", n);
	for (int i = 0; i < n; ++i) {
		printf("%d ", array[i]);
	}
	printf("\n");
}

int cmp_pair(const void* p1, const void* p2) {
	return *(int*)p1 - *(int*)p2;
}

int insert_int(int* tab, int n, int new_el) {
	int check = 1;
	for (int i = 0; i < n; i++) {
		if (tab[i] == new_el) {
			check = 0;
			break;
		}
	}
	return check;
}


int get_domain(pair* tab, int n, int* domain) {
	int el1, el2, i, cnt = 0;
	for (i = 0; i < n; i++) {
		el1 = tab[i].first;
		el2 = tab[i].second;
		if (insert_int(domain, cnt, el1))
			domain[cnt++] = el1;
		if (!(el1 == el2))
			if (insert_int(domain, cnt, el2))
				domain[cnt++] = el2;
	}
	qsort(domain, cnt, sizeof(int), cmp_pair);
	return cnt;
}



//------------------------------------------------

// Case 1:

// The relation R is reflexive if xRx for every x in X, X dziedzina relacji R
//Naddziedzinę (zbiór X) wyznaczamy jako unikalną tablicę poprzedników i następników
// par należących do relacji, czyli x i y-ki dodajemy
//a stricte równoważności (X,grR,X) to grR musi zawierać wszystkie X * X
//bo for all x,y in X a nie in grR, a tutaj akurat X definiujemy jako 
//zbiór x-sów i y-ków należacych po prostu do grR i to = X
// bo grR zawiera się w X*X tzn parach (x,y) należących do iloczynu kartezjańskiego X*X
// x należy do X i y należy do X (X,grR,X), więc x-sy suma y-ki dają nam X
//ale też jak mamy 1R3, 1R5, to teraz x,y w X to może być np (x,y) = (3,5)
// a jej nie ma w grR więc trzeba domain we wszystkich a nie tylko sprawdzać
// poprzez pary (x,y) w grR

int is_reflexive(pair* tab, int n) {
	int domain[MAX_REL_SIZE];
	int n_domain = get_domain(tab, n, domain);

	for (int i = 0; i < n_domain; i++) {
		int cnt = 0;

		for (int j = 0; j < n; j++) {
			if (tab[j].first == domain[i] && tab[j].second == domain[i])
				cnt = 1;
		}

		if (cnt == 0)
			return 0;
	}

	return 1;
}

// The relation R on the set X is called irreflexive
// if xRx is false for every x in X
int is_irreflexive(pair* tab, int n) {
	return 1 - is_reflexive(tab, n);
}

// A binary relation R over a set X is symmetric if:
// for all x, y in X xRy <=> yRx
int is_symmetric(pair* tab, int n) {
	for (int i = 0; i < n; i++) {
		int cnt = 0;
		for (int j = 0; j < n; j++) {//można j = i+1, bo dla xRx => xRx zawsze
			if (tab[j].first == tab[i].second && tab[j].second == tab[i].first)
				cnt = 1;
		}
		if (cnt == 0)
			return 0;
	}
	return 1;
}

// A binary relation R over a set X is antisymmetric if:
// for all x,y in X if xRy and yRx then x=y
int is_antisymmetric(pair* tab, int n) {
	int i, j, fir, sec, check;
	for (i = 0; i < n; i++) {
		fir = tab[i].first;
		sec = tab[i].second;
		check = 1;
		for (j = 0; j < n; j++) {
			if (tab[j].first == sec && tab[j].second == fir) {
				if (fir == sec) check = 1;
				else check = 0;
				break;
			}
		}
		if (!check) return 0;
	}
	return 1;
}

// A binary relation R over a set X is asymmetric if:
// for all x,y in X if at least one of xRy and yRx is false
int is_asymmetric(pair* tab, int n) {
	for (int i = 0; i < n; i++) {
		int cnt = 1;
		for (int j = 0; j < n; j++) {
			if (tab[j].first == tab[i].second && tab[j].second == tab[i].first)
				cnt = 0;
		}

		if (cnt == 0) //poza forem bo dla każdego x,y ma tak być że xRy => ~yRx
			return 0;
	}
	return 1;
}

// A homogeneous relation R on the set X is a transitive relation if:
// for all x, y, z in X, if xRy and yRz, then xRz
int is_transitive(pair* tab, int n) {
	int i, j, k, fir, sec, third, check;
	for (i = 0; i < n; i++) {
		fir = tab[i].first;
		sec = tab[i].second;
		check = 1;
		for (j = 0; j < n; j++) {
			if (tab[j].first == sec) {
				third = tab[j].second;
				check = 0;
				for (k = 0; k < n; k++) {
					if (tab[k].first == fir && tab[k].second == third) {
						check = 1;
						break;
					}
				}
				break;
			}
		}
		if (!check) return 0;
	}
	return 1;
}

//------------------------------------------------

// Case 2:

// A partial order relation is a homogeneous relation that is
// reflexive, transitive, and antisymmetric
int is_partial_order(pair* tab, int n) {
	return (is_reflexive(tab, n) && is_transitive(tab, n) && is_antisymmetric(tab, n));
}

// Relation R is connected if for each x, y in X:
// xRy or yRx (or both)
int is_connected(pair* tab, int n) {
	int domain[MAX_REL_SIZE];
	int n_domain = get_domain(tab, n, domain);
	for (int i = 0; i < n_domain; i++) {
		for (int j = 0; j < n_domain; j++) {
			int x = domain[i]; //dziedzina
			int y = domain[j];

			int cnt = 0;

			for (int k = 0; k < n; k++) {//również gdy xRy i yRx => x = y
				if ((tab[k].first == x && tab[k].second == y) || (tab[k].first == y && tab[k].second == x))
					cnt = 1;
			}
			if (cnt == 0)
				return 0;
		}
	}

	return 1;
}

// A total order relation is a partial order relation that is connected
int is_total_order(pair* tab, int n) {
	return (is_partial_order(tab, n) && is_connected(tab, n));
}

int find_max_elements(pair* tab, int n, int* max_elements) { // tab - partial order
	int i, j, elem, check, cnt = 0;
	for (i = 0; i < n; i++) {
		elem = tab[i].second;
		check = 1;
		for (j = 0; j < n; j++) {
			if (tab[j].first == elem) {
				if (tab[j].second != elem) {
					check = 0;
					break;
				}
			}
		}
		if (check) {
			if (insert_int(max_elements, cnt, elem))
				max_elements[cnt++] = elem;
		}
	}
	qsort(max_elements, cnt, sizeof(int), cmp_pair);
	return cnt;
}

int find_min_elements(pair* tab, int n, int* min) { // tab - strong partial order
	int i, j, elem, check, cnt = 0;
	for (i = 0; i < n; i++) {
		elem = tab[i].first;
		check = 1;
		for (j = 0; j < n; j++) {
			if (tab[j].second == elem) {
				if (tab[j].first != elem) {
					check = 0;
					break;
				}
			}
		}
		if (check) {
			if (insert_int(min, cnt, elem))
				min[cnt++] = elem;
		}
	}
	qsort(min, cnt, sizeof(int), cmp_pair);
	return cnt;
}

//------------------------------------------------

// Case 3:

// x(S o R)z iff exists y: xRy and ySz
int composition(pair* rel_1, int n1, pair* rel_2, int n2, pair* rel_3) {
	int cnt = 0;

	for (int i = 0; i < n1; i++) {
		for (int j = 0; j < n2; j++) {
			if (rel_1[i].second == rel_2[j].first) {
				pair p = { rel_1[i].first, rel_2[j].second };

				int found = 0;

				for (int k = 0; k < cnt; k++) {
					if (rel_3[k].first == p.first && rel_3[k].second == p.second)
						found = 1;
				}

				if (found == 0) {
					rel_3[cnt] = p;
					cnt++;
				}
			}
		}
	}

	return cnt;
}

int main(void) {
	int to_do;
	pair relation[MAX_REL_SIZE];
	pair relation_2[MAX_REL_SIZE];
	pair comp_relation[MAX_REL_SIZE];
	int domain[MAX_REL_SIZE];
	int max_elements[MAX_REL_SIZE];
	int min_elements[MAX_REL_SIZE];

	scanf("%d",&to_do);
	int size = read_relation(relation);
	int ordered, size_2, n_domain;
	int no_max_elements = find_max_elements(relation, size, max_elements);
	int no_min_elements = find_min_elements(relation, size, min_elements);
	switch (to_do) {
		case 1:
			printf("%d ", is_reflexive(relation, size));
			printf("%d ", is_irreflexive(relation, size));
			printf("%d ", is_symmetric(relation, size));
			printf("%d ", is_antisymmetric(relation, size));
			printf("%d ", is_asymmetric(relation, size));
			printf("%d\n", is_transitive(relation, size));
			break;
		case 2:
			ordered = is_partial_order(relation, size);
			n_domain = get_domain(relation, size, domain);
			printf("%d %d\n", ordered, is_total_order(relation, size));
			print_int_array(domain, n_domain);
			if (!ordered) break;
			print_int_array(max_elements, no_max_elements);
			print_int_array(min_elements, no_min_elements);
			break;
		case 3:
			size_2 = read_relation(relation_2);
			printf("%d\n", composition(relation, size, relation_2, size_2, comp_relation));
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	
	return 0;
}

