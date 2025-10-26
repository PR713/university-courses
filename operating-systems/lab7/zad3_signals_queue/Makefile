CC = gcc
CFLAGS = -Wall -g
TARGET = signals

SIGUSR1 := $(shell kill -l SIGUSR1)
SIGUSR2 := $(shell kill -l SIGUSR2)

all: $(TARGET)

$(TARGET): $(TARGET).o
	$(CC) $(CFLAGS) -o $@ $^

$(TARGET).o: main.c
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(TARGET) *.o output.txt tmp.txt

test: test_valid_signals test_invalid_args test_non_numeric_value

test_valid_signals:
	@echo "Test 1: Sending SIGUSR1 with value 123"
	-@./$(TARGET) 123 $(SIGUSR1) && echo "\033[0;32m✓ OK\033[0m" || echo "\033[0;31m✗ FAIL\033[0m"
	@echo "Test 2: Sending SIGUSR2 with value 456"
	-@./$(TARGET) 456 $(SIGUSR2) && echo "\033[0;32m✓ OK\033[0m" || echo "\033[0;31m✗ FAIL\033[0m"

test_invalid_args:
	@echo "Test 3: Invalid number of arguments"
	-@./$(TARGET) 123 ; if [ $$? -eq 1 ]; then echo "\033[0;32m✓ OK\033[0m"; else echo "\033[0;31m✗ FAIL\033[0m"; fi

test_non_numeric_value:
	@echo "Test 4: Non-numeric value 'abc'"
	-@./$(TARGET) abc $(SIGUSR1) 2>&1 | grep -q "numeric" && echo "\033[0;32m✓ OK\033[0m" || echo "\033[0;31m✗ FAIL\033[0m"

