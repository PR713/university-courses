CC = gcc
CFLAGS = -std=c17 -Wall

all: main catcher sender

main:
	${CC} ${CFLAGS} main.c -o main

catcher:
	${CC} ${CFLAGS} catcher.c -o catcher

sender:
	${CC} ${CFLAGS} sender.c -o sender

clean: 
	rm -f main catcher sender

.PHONY: clean all 