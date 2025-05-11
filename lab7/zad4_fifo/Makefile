CC=gcc
CFLAGS=-Wall -g

all: reader writer

reader: reader.c
	$(CC) $(CFLAGS) -o reader reader.c

writer: writer.c
	$(CC) $(CFLAGS) -o writer writer.c

clean:
	rm -f reader writer reader_wzor writer_wzor myfifo

test:
	@echo "========== TEST ==========\n"
	chmod +x test.sh
	./test.sh


