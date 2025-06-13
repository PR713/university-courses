#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define IN_LINE_COMMENT 1
#define IN_BLOCK_COMMENT 2
#define IN_STRING 4
#define IN_ID 8

#define MAX_ID_LEN 64
#define MAX_IDS 1024

int index_cmp(const void*, const void*);
int cmp(const void*, const void*);

char identifiers[MAX_IDS][MAX_ID_LEN];

const char *keywords[] = {
	"auto", "break", "case", "char",
	"const", "continue", "default", "do",
	"double", "else", "enum", "extern",
	"float", "for", "goto", "if",
	"int", "long", "register", "return",
	"short", "signed", "sizeof", "static",
	"struct", "switch", "typedef", "union",
	"unsigned", "void", "volatile", "while"
};

int found(char word[], int in_tab) {
	int size = sizeof(keywords) / sizeof(keywords[0]);
	for (int i = 0; i < size; i++) {
		if (strcmp(word, keywords[i]) == 0) return 0;
	}
	for (int i = 0; i < in_tab; i++) {
		if (strcmp(word, identifiers[i]) == 0) return 0;
	}
	return 1;
}

int find_idents() {
	int i, index = 0, cnt = 0;
	char a, b = fgetc(stdin);
	while (b != EOF) {
		if (b == '\'') {//czy apostrof
			b = fgetc(stdin);
			while (b != '\'') {
				if (b == '\\') fgetc(stdin); //czy b == '\'
				b = fgetc(stdin); //^ przejście do nowej linii
			}
		}
		else if (b == '"') { //czy cudzysłów
			b = fgetc(stdin);
			while (b != '"') {
				if (b == '\\') fgetc(stdin);
				b = fgetc(stdin);
			}
		}
		else if (b == '_' || isalpha(b)) {//czy znak podkreślnika
			i = 0;
			while (b == '_' || isalnum(b)) {
				identifiers[index][i] = b;
				i++;
				b = fgetc(stdin);
			}

			cnt += found(identifiers[index], index);
			index++;
		}
		else if (b == '/') { // czy komentarz blokowy
			a = fgetc(stdin);
			if (a == '/') while (b != '\r' && b != '\n') b = fgetc(stdin);
			else if (a == '*') {
				while (!(b == '*' && a == '/')) {//gdy oba prawdziwe przerwie
					b = a;
					a = fgetc(stdin);
				}
			}
		}
		b = fgetc(stdin);
	}
	return cnt;
}

int cmp(const void* first_arg, const void* second_arg) {
	char *a = *(char**)first_arg;
	char *b = *(char**)second_arg;
	return strcmp(a, b);
}

int index_cmp(const void* first_arg, const void* second_arg) {
	int a = *(int*)first_arg;
	int b = *(int*)second_arg;
	return strcmp(identifiers[a], identifiers[b]);
}

int main(void) {
	printf("%d\n", find_idents());
	return 0;
}

