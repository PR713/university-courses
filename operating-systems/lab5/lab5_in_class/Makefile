CC = gcc
CFLAGS = -std=c17 -Wall

all: kart main kill raise fork_signal


kart:
	${CC} ${CFLAGS} kart.c -o kart


main:
	${CC} ${CFLAGS} main.c -o main

raise:
	${CC} ${CFLAGS} raise.c -o raise 

kill:
	${CC} ${CFLAGS} kill.c -o kill

fork_signal:
	${CC} ${CFLAGS} fork_signal.c -o fork_signal

clean: 
	rm -f kart main raise kill fork_signal

.PHONY: clean all 