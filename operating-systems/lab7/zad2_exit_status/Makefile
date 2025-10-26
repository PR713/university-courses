CC = gcc
CFLAGS = -Wall -g
TARGET = exit_status

.PHONY: all clean run test

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) -o $@ $<

run: $(TARGET)
	./$(TARGET)

test:
	@echo "========== TEST =========="
	./$(TARGET) > output.txt 2>&1 || true
	@echo "========== OUTPUT =========="
	@cat output.txt
	@echo "========== EXIT CODE =========="
	@echo $$?

clean:
	rm -f $(TARGET) *.o output.txt