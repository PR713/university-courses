#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct {
	int day; 
	int month; 
	int year;
} Date;

// 1 bsearch2

#define NAME_MAX  20   // max. length of name + 1
#define FOOD_MAX  30   // max. number of goods
#define RECORD_MAX 64  // max. line length

typedef struct {
	char name[NAME_MAX];
	float price;
	int amount;
	Date valid_date;
} Food;

typedef int (*ComparFp)(const void *, const void *);

int cmp_date(const void *d1, const void *d2) {
	Date *p1 = (Date*) d1;
	Date *p2 = (Date*) d2;

	int cond = p1->year - p2->year;
	if(cond != 0) {
		return cond;
	}

	cond = p1->month - p2->month;
	if(cond != 0) {
		return cond;
	}

	cond = p1->day - p2->day;
	return cond;
}

int cmp(const void *a, const void *b) {
	Food* p1 = (Food*) a;
	Food* p2 = (Food*) b;
	int cond = strcmp(p1->name, p2->name);
	if(cond != 0) {
		return cond;
	}
	float f_cond = p1->price - p2->price;
	if(f_cond < 0.f) {
		return -1;
	}
	if(f_cond > 0.f) {
		return 1;
	}

	cond = cmp_date((void*)&p1->valid_date, (void*)&p2->valid_date);
	return cond;
}

void* get_address_from_index(void *base, size_t element_size, size_t index) {
	return base + element_size * index;
}

void* bsearch2 (const void *key, void *base, int n_items, size_t size, ComparFp compar, char *result) {
	int l = 0, r = n_items - 1;
	int ans = r;
	while( l <= r ) {
		int mid = l + (r - l) / 2;
		void *mid_ele = get_address_from_index(base, size, mid);

		int cond = compar(mid_ele, key );

		if(cond == 0) {
			*result = 1;
			return mid_ele;
		}

		if(cond < 0) {
			ans = mid;
			l = mid + 1;
		}else {
			r = mid - 1;
		}
	}

	++ans;
	*result = 0;
	return get_address_from_index(base, size, ans);
}

void print_art(Food *p, const int n, const char *art) {
	for(int i = 0; i < n; ++i) {
		if(strcmp(p->name, art) == 0) {
			printf(
				"%.2f %d %02d.%02d.%d\n",
				p->price,
				p->amount,
				p->valid_date.day,
				p->valid_date.month,
				p->valid_date.year
			);
		}
		++p;
	}
}

Food* add_record(Food *tab, int *np, const ComparFp compar, const Food *new) {
	char result = '\0';
	Food* ptr = (Food*)bsearch2(new, tab, *np, sizeof(*new), compar, &result);

	if(result == 0) {
		memmove((void*)(ptr + 1), (void*)ptr, (&tab[*np - 1] - ptr + 1) * sizeof(*new));
		*ptr = *new;
		*np += 1;
	}else {
		ptr->amount += new->amount; 
	}

	return ptr;
}

int read_goods(Food *tab, const int no, FILE *stream, const int sorted) {
	Food new;
	int np = 0;
	for(int i = 0; i < no; ++i) {
		fscanf(
			stream,
			"%s %f %d %d.%d.%d",
			new.name,
			&new.price,
			&new.amount,
			&new.valid_date.day,
			&new.valid_date.month,
			&new.valid_date.year
		);
		if(sorted) {
			add_record(tab, &np, cmp, &new);
		}else {
			tab[np] = new;
			++np;
		}
	}
	return np;
}

int cmp_qs(const void *a, const void *b) {
	const Food *fa = (Food*)a, *fb = (Food*)b;
	return cmp_date(&fa->valid_date, &fb->valid_date);
}

int cmp_bs(const void *a, const void *b) {
	const Date *pd = (Date*)a;
	const Food *fb = (Food*)b;
	return cmp_date(pd, &fb->valid_date);
}

void date_to_tm(Date* date, struct tm* tm_ptr) {
	memset(tm_ptr, 0, sizeof(struct tm));
	tm_ptr->tm_mday = date->day;
	tm_ptr->tm_mon = date->month - 1;
	tm_ptr->tm_year = date->year - 1900;
	tm_ptr->tm_isdst = -1;
}

int cmp_tm(const void *a, const void *b) {
	Food* p1 = (Food*) a;
	Food* p2 = (Food*) b;
	struct tm tm1;
	struct tm tm2;
	date_to_tm(&p1->valid_date, &tm1);
	date_to_tm(&p2->valid_date, &tm2);
	return mktime(&tm1) - mktime(&tm2);
}

float value(Food *food_tab, const size_t n, const Date curr_date, const int days) {
	qsort(food_tab, n, sizeof(Food), cmp_tm);
	Date keyDate = curr_date;
	keyDate.day += days;
	Food keyFood;
	keyFood.valid_date = keyDate;
	Food *ptr = (Food*)bsearch(&keyFood, food_tab, n, sizeof(Food), cmp_tm);
	if(ptr == NULL) {
		return 0.f;
	}
	float ans = 0.f;
	
	for(Food *itr = ptr; itr <= &food_tab[n-1] && cmp_date(itr, ptr) == 0; ++itr) {
		ans += itr->amount * itr->price;
	}

	for(Food *itr = ptr - 1; itr >= food_tab && cmp_date(itr, ptr) == 0; --itr) {
		ans += itr->amount * itr->price;
	}

	return ans;
}

/////////////////////////////////////////////////////////////////
// 3 Succession

#define CHILD_MAX  20
#define PERSON_TAB_SIZE 34

enum Sex {F, M};
enum BOOL {no, yes};

struct Bit_data {
    enum Sex sex:1;
    enum BOOL pretendent:1;
};

typedef struct {
    char *name;
    struct Bit_data bits;
    Date born;
    char *parent;
} Person;

typedef struct {
    char *par_name;
    int ind_first;
    int ind_last;
} Parent;

const Date primo_date = { 28, 10, 2011 };

int person_cmp_parent(const void* _a, const void* _b){
    Person a = *((Person*)_a);
    Person b = *((Person*)_b);

    if(a.parent == NULL)
        return 1;
    if(b.parent == NULL)
        return -1;

    return strcmp(a.parent, b.parent);
}

int parent_cmp(const void* _a, const void* _b){
    Parent a = *((Parent*)_a);
    Parent b = *((Parent*)_b);

    return strcmp(a.par_name, b.par_name);
}

int fill_indices_tab(Parent *idx_tab, Person *pers_tab, int size) {
    int no_parents = 0;

    for(int i = 0; i < size; i++){
        int found = 0;

        for(int u = 0; u < no_parents; u++){
            if(strcmp(pers_tab[i].name, idx_tab[u].par_name) == 0){
                found = 1;
                break;
            }
        }

        if(!found){
            idx_tab[no_parents].par_name = pers_tab[i].name;

            Person key = { .parent = pers_tab[i].name};

            Person* address = bsearch(&key, pers_tab, size, sizeof(Person), person_cmp_parent);

            if(address == NULL)
                continue;

            int index = (int)(address - pers_tab);
            int tmp = index;

            while(tmp > 0 && person_cmp_parent(&pers_tab[tmp], &pers_tab[tmp-1]) == 0) tmp--;

            idx_tab[no_parents].ind_first = tmp;
            tmp = index;

            while(tmp < size - 1 && person_cmp_parent(&pers_tab[tmp], &pers_tab[tmp+1]) == 0) tmp++;

            idx_tab[no_parents].ind_last = tmp;
            no_parents++;
        }
    }

    qsort(idx_tab, no_parents, sizeof(Parent), parent_cmp);

    return no_parents;
}

void persons_shiftings(Person *person_tab, int size, Parent *idx_tab, int no_parents) {
    int index = 0;

    Person tmp[PERSON_TAB_SIZE];

    while (index < size){
        Parent key = {.par_name = person_tab[index].name};
        Parent* address = bsearch(&key, idx_tab, no_parents, sizeof(Parent), parent_cmp);

        if(address != NULL) {
            int to_copy = address->ind_last - address->ind_first + 1;

            memmove(tmp, &person_tab[address->ind_first], to_copy * sizeof(Person));
            memmove(&person_tab[index + to_copy + 1], &person_tab[index + 1],
                    ((address->ind_first) - index - 1) * sizeof(Person));
            memmove(&person_tab[index + 1], tmp, to_copy * sizeof(Person));

            for(int i = 0; i < no_parents; i++){
                if(idx_tab[i].ind_first < address->ind_first) {
                    idx_tab[i].ind_first += to_copy;
                    idx_tab[i].ind_last += to_copy;
                }
            }
        }

        index += 1;
    }
}

int cleaning(Person *person_tab, int n) {
    for(int i = 0; i < n; i++){
        if(person_tab[i].bits.pretendent == no){
            memmove(&person_tab[i], &person_tab[i + 1], (n - i)*sizeof(Person));
            i--;
            n--;
        }
    }

    return n;
}

void print_person(const Person *p) {
    printf("%s\n", p->name);
}

void print_persons(const Person *person_tab, int n) {
    for(int i=1; i<=n; ++i, ++person_tab) printf("%2d %12s %s\n", i, person_tab->name, person_tab->parent);
}

int compare(const void* _a, const void* _b){
    Person a = *((Person*)_a);
    Person b = *((Person*)_b);

    if(a.parent == NULL)
        return -1;
    if(b.parent == NULL)
        return 1;

    int parent = strcmp(a.parent, b.parent);

    if(parent < 0)
        return -1;
    else if(parent > 0)
        return 1;
    else {
        int born_date = cmp_date(&a.born, &b.born);

        if(cmp_date(&a.born, &primo_date) < 0 && cmp_date(&b.born, &primo_date) < 0) {
            if (a.bits.sex == M && b.bits.sex == F)
                return -1;
            else if (a.bits.sex == F && b.bits.sex == M)
                return 1;
        }

        if(born_date < 0)
            return -1;
        else if(born_date > 0)
            return 1;
        else {
            if (a.bits.sex > b.bits.sex)
                return 1;
            else if (a.bits.sex < b.bits.sex)
                return -1;
            else
                return 0;
        }
    }
}

int create_list(Person *person_tab, int n) {
    qsort(person_tab, n, sizeof(Person), compare);

    Parent parents_tab[PERSON_TAB_SIZE];

    int no_parents = fill_indices_tab(parents_tab, person_tab, n);

    persons_shiftings(person_tab, n, parents_tab, no_parents);

    return cleaning(person_tab, n);
}

int main(void) {
	Person person_tab[PERSON_TAB_SIZE] = {
		{"Charles III", {M, no}, {14, 11, 1948},"Elizabeth II"},
		{"Anne", {F,yes}, {15, 8, 1950},"Elizabeth II"},
		{"Andrew", {M,yes}, {19, 2, 1960},"Elizabeth II"},
		{"Edward", {M,yes}, {10, 3, 1964} ,"Elizabeth II"},
		{"David", {M,yes}, {3, 11, 1961} ,"Margaret"},
		{"Sarah", {F,yes}, {1, 5, 1964}, "Margaret"},
		{"William", {M,yes}, {21, 6, 1982}, "Charles III"},
		{"Henry", {M,yes}, {15, 9, 1984}, "Charles III"},
		{"Peter", {M,yes}, {15, 11, 1977}, "Anne"},
		{"Zara", {F,yes}, {15, 5, 1981}, "Anne"},
		{"Beatrice", {F,yes}, {8, 8, 1988}, "Andrew"},
		{"Eugenie", {F,yes}, {23, 3, 1990}, "Andrew"},
		{"James", {M,yes}, {17, 12, 2007}, "Edward"},
		{"Louise", {F,yes}, {8, 11, 2003}, "Edward"},
		{"Charles", {M,yes}, {1, 7, 1999}, "David"},
		{"Margarita", {F,yes}, {14, 5, 2002}, "David"},
		{"Samuel", {M,yes}, {28, 7, 1996}, "Sarah"},
		{"Arthur", {M,yes}, {6, 5, 2019}, "Sarah"},
		{"George", {M,yes}, {22, 7, 2013}, "William"},
		{"George VI", {M,no}, {14, 12, 1895}, NULL},
		{"Charlotte", {F,yes}, {2, 5, 2015}, "William"},
		{"Louis", {M,yes}, {23, 4, 2018}, "William"},
		{"Archie", {M,yes}, {6, 5, 2019}, "Henry"},
		{"Lilibet", {F,yes}, {4, 6, 2021}, "Henry"},
		{"Savannah", {F,yes}, {29, 12, 2010}, "Peter"},
		{"Isla", {F,yes}, {29, 3, 2012}, "Peter"},
		{"Mia", {F,yes}, {17, 1, 2014}, "Zara"},
		{"Lena", {F,yes}, {18, 6, 2018}, "Zara"},
		{"Elizabeth II", {F,no}, {21, 4, 1926}, "George VI"},
		{"Margaret", {F,no}, {21, 8, 1930}, "George VI"},
		{"Lucas", {M,yes}, {21, 3, 2021}, "Zara"},
		{"Sienna", {F,yes}, {18, 9, 2021}, "Beatrice"},
		{"August", {M,yes}, {9, 2, 2021}, "Eugenie"},
		{"Ernest", {M,yes}, {30, 5, 2023}, "Eugenie"}
	};

	int to_do, no;
	int n;
	Food food_tab[FOOD_MAX];
	char buff[RECORD_MAX];
	fgets(buff, RECORD_MAX, stdin);
	sscanf(buff, "%d", &to_do);

	switch (to_do) {
		case 1:  // bsearch2
			fgets(buff, RECORD_MAX, stdin);
			sscanf(buff, "%d", &no);
			n = read_goods(food_tab, no, stdin, 1);
			scanf("%s",buff);
			print_art(food_tab, n, buff);
			break;
		case 2: // qsort
			fgets(buff, RECORD_MAX, stdin);
			sscanf(buff, "%d", &no);
			n = read_goods(food_tab, no, stdin, 0);
			Date curr_date;
			int days;
			scanf("%d %d %d", &curr_date.day, &curr_date.month, &curr_date.year);
			scanf("%d", &days);
			printf("%.2f\n", value(food_tab, (size_t)n, curr_date, days));
			break;
		case 3: // succession
			scanf("%d", &no);
			const int no_persons = sizeof(person_tab) / sizeof(Person);
			create_list(person_tab,no_persons);
			print_person(person_tab + no - 1);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
	}
	return 0;
}