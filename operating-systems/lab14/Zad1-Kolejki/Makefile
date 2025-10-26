CC = gcc
CFLAGS = -Wall
TARGET = main

.PHONY: all clean test

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) -o $(TARGET) main.c

clean:
	rm -f $(TARGET) test*.out

test: $(TARGET)
	@echo "== Test: input=0, expected=10 =="
	@out=$(shell ./$(TARGET) 0); \
	echo "ℹ️  input=0, expected=10, received=$$out"; \
	[ "$$out" = "10" ] && echo "✅ Test passed" || (echo "❌ Test failed"; exit 1)

	@echo "== Test: input=5, expected=15 =="
	@out=$(shell ./$(TARGET) 5); \
	echo "ℹ️  input=5, expected=15, received=$$out"; \
	[ "$$out" = "15" ] && echo "✅ Test passed" || (echo "❌ Test failed"; exit 1)

	@echo "== Test: input=42, expected=52 =="
	@out=$(shell ./$(TARGET) 42); \
	echo "ℹ️  input=42, expected=52, received=$$out"; \
	[ "$$out" = "52" ] && echo "✅ Test passed" || (echo "❌ Test failed"; exit 1)

	@echo "== Test: input=-123, expected=-113 =="
	@out=$(shell ./$(TARGET) -123); \
	echo "ℹ️  input=-123, expected=-113, received=$$out"; \
	[ "$$out" = "-113" ] && echo "✅ Test passed" || (echo "❌ Test failed"; exit 1)

	@echo "== Test: input=999999, expected=1000009 =="
	@out=$(shell ./$(TARGET) 999999); \
	echo "ℹ️  input=999999, expected=1000009, received=$$out"; \
	[ "$$out" = "1000009" ] && echo "✅ Test passed" || (echo "❌ Test failed"; exit 1)

	@echo "== Test: invalid input 'abc' (should error) =="
	@./$(TARGET) abc > /dev/null 2>&1 && (echo "❌ Test failed: program should have rejected invalid input"; exit 1) || echo "✅ Invalid input correctly rejected"