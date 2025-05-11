CC = gcc
CFLAGS = -Wall -Wextra -std=c99
TARGET = main
OUT = output.txt

.PHONY: all clean run test

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

run: $(TARGET)
	./$(TARGET)

test: $(TARGET)
	@echo "========== TEST =========="
	./$(TARGET) > $(OUT) 2>&1 || true
	@echo "========== OUTPUT =========="
	@cat $(OUT)
	@echo "========== EXIT CODE =========="
	@echo $$?

