CC = gcc
CFLAGS = -std=c17 -Wall

all: init printer user

printer:
	${CC} ${CFLAGS} printer.c -o printer

user:
	${CC} ${CFLAGS} user.c -o user

clean: 
	rm -f init printer user

.PHONY: clean all 