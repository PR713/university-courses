#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

// consider chars from [FIRST_CHAR, LAST_CHAR)
#define FIRST_CHAR 33
#define LAST_CHAR 127
#define MAX_CHARS (LAST_CHAR - FIRST_CHAR)
#define MAX_BIGRAMS ((LAST_CHAR - FIRST_CHAR) * (LAST_CHAR - FIRST_CHAR))

#define NEWLINE '\n'
#define IN_WORD 1

#define IN_LINE_COMMENT 1
#define IN_BLOCK_COMMENT 2

int count[MAX_BIGRAMS] = { 0 };

// sort indices according to their respective counts.
// sort alphabetically if counts equal
int cmp (const void *a, const void *b) {
	int va = *(int*)a;
	int vb = *(int*)b;
	if (count[va] == count[vb]) return va - vb;	return count[vb] - count[va];
}

// sort indices according to their respective counts.
// sort alphabetically if counts equal
int cmp_di (const void *a, const void *b) {
	int va = *(int*)a;
	int vb = *(int*)b;
	// sort according to second char if counts and the first char equal
	if (count[va] == count[vb] && va / MAX_CHARS == vb / MAX_CHARS) return va % MAX_CHARS - vb % MAX_CHARS;
	// sort according to first char if counts equal
	if (count[va] == count[vb]) return va / MAX_CHARS - vb / MAX_CHARS;
	return count[vb] - count[va];
}

// count lines, words & chars in a given text file
void wc(int *nl, int *nw, int *nc, FILE *stream) {
	*nl = *nw = *nc = 0;
	char c = fgetc(stream);
	int spaces_after_word = 0; //spacje, flaga
	while (c != EOF) { //dopóki nie skończy się tekst
		*nc += 1;
		if (isspace(c)) {
			if (c == '\n') *nl += 1;
			if (spaces_after_word == 1) *nw += 1;
			spaces_after_word = 0;
		}
		else spaces_after_word = 1;//jeśli wyraz się nie skończył
		c = fgetc(stream);
	}
}

void char_count(int char_no, int *n_char, int *cnt, FILE *stream) {
	int chars[MAX_CHARS];
	for (int i = 0; i < MAX_CHARS; i++) {
		chars[i] = i;
		count[i] = 0;
	}
	char c = fgetc(stream);
	while (c != EOF) {
		if (c >= FIRST_CHAR && c < LAST_CHAR) count[c - FIRST_CHAR] += 1;
		c = fgetc(stream);
	}
	qsort(chars, MAX_CHARS, sizeof(int), cmp);
	*n_char = FIRST_CHAR + chars[char_no - 1];
	*cnt = count[*n_char - FIRST_CHAR];
}

void bigram_count(int bigram_no, int bigram[], FILE *stream) {
	int bigrams[MAX_BIGRAMS];
	for (int i = 0; i < MAX_CHARS; i++)
		for (int j = 0; j < MAX_CHARS; j++)
			bigrams[i * MAX_CHARS + j] = i * MAX_CHARS + j;

	char a, b = fgetc(stream);
	while (b != EOF) {
		a = fgetc(stream);
		if (b >= FIRST_CHAR && b < LAST_CHAR && a >= FIRST_CHAR && a < LAST_CHAR)
			count[(b - FIRST_CHAR) * MAX_CHARS + a - FIRST_CHAR] += 1;
		b = a;
	}
	qsort(bigrams, MAX_BIGRAMS, sizeof(int), cmp_di);
	bigram[0] = FIRST_CHAR + bigrams[bigram_no - 1] / MAX_CHARS;
	bigram[1] = FIRST_CHAR + bigrams[bigram_no - 1] % MAX_CHARS;
	bigram[2] = count[(bigram[0] - FIRST_CHAR) * MAX_CHARS + bigram[1] - FIRST_CHAR];
}

void find_comments(int *line_comment_counter, int *block_comment_counter, FILE *stream) {
	char a, b = fgetc(stream);
	*line_comment_counter = *block_comment_counter = 0;
	while (b != EOF) {
		a = getc(stream); //drugi
		if (b == '/') {
			if (a == '/') {
				while (fgetc(stream) != '\n');
				*line_comment_counter += 1;
			}
			else if (a == '*') {
				while (!(b == '*' && a == '/')) {
					b = a;
					a = fgetc(stream);
				}
				*block_comment_counter += 1;
			}
			a = fgetc(stream);
		}
		b = a;
	}
}

#define MAX_LINE 128

int read_int() {
	char line[MAX_LINE];
	fgets(line, MAX_LINE, stdin); // to get the whole line
	return (int)strtol(line, NULL, 10);
}

int main(void) {
	int to_do;
	int nl, nw, nc, char_no, n_char, cnt;
	int line_comment_counter, block_comment_counter;
	int bigram[3];

	FILE* stream;
	stream = stdin;
	to_do = read_int();
	switch (to_do) {
		case 1: // wc()
			wc (&nl, &nw, &nc, stream);
			printf("%d %d %d\n", nl, nw, nc);
			break;
		case 2: // char_count()
			char_no = read_int();
			char_count(char_no, &n_char, &cnt,stream);
			printf("%c %d\n", n_char, cnt);
			break;
		case 3: // bigram_count()
			char_no = read_int();
			bigram_count(char_no, bigram, stream);
			printf("%c%c %d\n", bigram[0], bigram[1], bigram[2]);
			break;
		case 4:
			find_comments(&line_comment_counter, &block_comment_counter, stream);
			printf("%d %d\n", block_comment_counter, line_comment_counter);
			break;
		default:
			printf("NOTHING TO DO FOR %d\n", to_do);
			break;
	}
	return 0;
}

