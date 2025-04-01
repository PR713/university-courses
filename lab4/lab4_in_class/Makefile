CC = gcc
CFLAGS = -std=c17 -Wall -g

all: main counter

main: 
	${CC} ${CFLAGS}	main.c -o main

counter: 
	${CC} ${CFLAGS}	counter.c -o counter



clean: 
	rm -f main counter

.PHONY: clean all