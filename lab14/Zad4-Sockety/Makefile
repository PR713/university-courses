CC = gcc
CFLAGS = -Wall -O2

SERVER = server
CLIENT = client

all: $(SERVER) $(CLIENT)

$(SERVER): server.c
	$(CC) $(CFLAGS) -o $(SERVER) server.c

$(CLIENT): client.c
	$(CC) $(CFLAGS) -o $(CLIENT) client.c

clean:
	rm -f $(SERVER) $(CLIENT) *.out *.log

test: all
	@chmod +x run_tests.sh
	@./run_tests.sh > test.log 2>&1
	@cat test.log