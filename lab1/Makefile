CC = gcc
CFLAGS = -std=c17 -Wall -g

all: countdown 

countdown: countdown.c
		$(CC) $(CFLAGS) countdown.c -o countdown

clean: 
		rm -f countdown

.PHONY: clean all