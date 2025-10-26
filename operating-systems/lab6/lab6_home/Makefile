CC = gcc
CFLAGS = -std=c17 -Wall

all: zad1 zad2 zad2sender

zad1: 
	${CC} ${CFLAGS} zad1.c -o zad1

zad2:
	${CC} ${CFLAGS} zad2.c -o zad2

zad2sender:
	${CC} ${CFLAGS} zad2sender.c -o zad2sender

clean: 
	rm -f zad1 zad2 zad2sender


.PHONY: clean all