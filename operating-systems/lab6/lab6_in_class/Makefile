CC = gcc
CFLAGS = -std=c17 -Wall

all: kartkowka sender receiver progA

kartkowka:
	${CC} ${CFLAGS} kartkowka.c -o kartkowka

sender:
	${CC} ${CFLAGS} sender.c -o sender

receiver:
	${CC} ${CFLAGS} receiver.c -o receiver

progA:
	${CC} ${CFLAGS} progA.c -o progA


clean: 
	rm -f kartkowka sender receiver progA

.PHONY: clean all 