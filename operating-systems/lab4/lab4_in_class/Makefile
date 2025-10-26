CC = gcc
CFLAGS = -std=c17 -Wall -g

all: main counter cos

main: 
	${CC} ${CFLAGS}	main.c -o main

counter: 
	${CC} ${CFLAGS}	counter.c -o counter

cos:
	${CC} ${CFLAGS} cos.c -o cos

clean: 
	rm -f main counter cos

.PHONY: clean all