CC = gcc
CFLAGS = -Wall -pthread

SYNC_EXEC = main

all: $(SYNC_EXEC)

$(SYNC_EXEC): main.c
	$(CC) $(CFLAGS) -o $(SYNC_EXEC) main.c

test: $(SYNC_EXEC)
	@chmod +x run_test.sh
	@./run_test.sh > test.log 2>&1
	@cat test.log

clean:
	rm -f $(SYNC_EXEC) *.log *.out