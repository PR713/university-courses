CC = gcc
CFLAGS = -Wall -pthread

TARGET = main

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

clean:
	rm -f $(TARGET) *.out *.log

test: all
	@chmod +x run_tests.sh
	@./run_tests.sh > test.log 2>&1
	@cat test.log