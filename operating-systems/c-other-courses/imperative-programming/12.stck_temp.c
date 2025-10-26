#include <stdio.h>

#define STACK_SIZE 10

enum state { OK = 0, UNDERFLOW = -1, OVERFLOW = -2 };

int stack[STACK_SIZE];
int top = 0;

int stack_push(int x) {
	if (top == STACK_SIZE) return OVERFLOW;
	else {
		stack[top++] = x;
		return OK;
	}
}

int stack_pop(void) {
	if (top == 0) return UNDERFLOW;
	else return stack[--top];
}

int stack_state(void) {
	return top;
}

// FIFO queue with shifts

#define QUEUE_SIZE 10

int queue[QUEUE_SIZE];
int in = 0, curr_nr = 0;

int queue_push(int in_nr) { // in_nr clients try to enter the queue
	for (int i = 0; i < in_nr; i++) {
		if (in == QUEUE_SIZE) {
			curr_nr += (in_nr - i); //tyle zostało przesuwamy dla kolejnych klientów numer
			return OVERFLOW;
		}
		queue[in++] = ++curr_nr;
	}
	return OK;
}

int queue_pop(int out_nr) { // out_nr clients leaves the queue
	if (out_nr > in) {
		in = 0;
		return UNDERFLOW;
	}
	else {
		for (int i = 0; i < in - out_nr; i++) {
			queue[i] = queue[i + out_nr];
		}
		in -= out_nr;
		return in;
	}
}

int queue_state(void) {
	return in;
}

void queue_print(void) {
	for (int i = 0; i < in; i++) printf("%d ", queue[i]);
	printf("\n");
}

// Queue with cyclic buffer

#define CBUFF_SIZE 10

int cbuff[CBUFF_SIZE];
int out = 0, len = 0;


int cbuff_push(int cli_nr) { // client with number cli_nr enters the queue
	if (len == CBUFF_SIZE) return OVERFLOW;
	else {
		cbuff[(out + len++) % CBUFF_SIZE] = cli_nr;
		return OK;
	}
}


int cbuff_pop(void) { // longest waiting client leaves the queue
	if (len == 0) return UNDERFLOW;
	else {
		out++;
		len--;
		return cbuff[out - 1];
	}
}

int cbuff_state(void) {
	return len;
}

void cbuff_print(void) {
	for (int i = 0; i < len; i++) printf("%d ", cbuff[(out + i) % CBUFF_SIZE]);
	printf("\n");
}

int main(void) {
	int to_do, n, client_no, answer;
	scanf_s("%d", &to_do);
	switch (to_do) {
	case 1: // stack
		do {
			scanf_s("%d", &n);
			if (n > 0) {
				if ((answer = stack_push(n)) < 0) printf("%d ", answer);
			}
			else if (n < 0) {
				printf("%d ", stack_pop());
			}
			else printf("\n%d\n", stack_state());
		} while (n != 0);
		break;
	case 2: // FIFO queue with shifts
		do {
			scanf_s("%d", &n);
			if (n > 0) {
				if ((answer = queue_push(n)) < 0) printf("%d ", answer);
			}
			else if (n < 0) {
				if ((answer = queue_pop(-n)) < 0) printf("%d ", answer);
			}
			else {
				printf("\n%d\n", queue_state());
				queue_print();
			}
		} while (n != 0);
		break;
	case 3: // queue with cyclic buffer
		client_no = 0;
		do {
			scanf_s("%d", &n);
			if (n > 0) {
				if ((answer = cbuff_push(++client_no)) < 0) printf("%d ", answer);
			}
			else if (n < 0) {
				printf("%d ", cbuff_pop());
			}
			else {
				printf("\n%d\n", cbuff_state());
				cbuff_print();
			}
		} while (n != 0);
		break;
	default:
		printf("NOTHING TO DO!\n");
	}
	return 0;
}
