//SOCK_STREAM
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <signal.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <fcntl.h>

#define MAX_CLIENTS 10
#define MAX_NAME 32
#define BUFFER_SIZE 256
#define ALIVE_INTERVAL 10

typedef enum {
    CMD_LIST,
    CMD_TOALL,
    CMD_TOONE,
    CMD_STOP,
    CMD_INVALID
} CommandType;


typedef struct {
    int sockfd;
    char name[MAX_NAME];
    time_t last_alive;
} Client;

Client clients[MAX_CLIENTS] = {0};

int server_socket;


int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <port>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    signal(SIGINT, signal_handler);

    int port = atoi(argv[1]);
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);

    server_socket = -1;
    if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Error creating socket");
    }

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    addr.sin_addr.s_addr = inet_addr("127.0.0.5");

    if (bind(server_socket, (struct sockaddr *)&addr, sizeof(struct sockaddr)) == -1) {
        perror("Error binding");
    }

    listen(server_socket, MAX_CLIENTS);

    printf("Server started on port %d\n", port);

    fd_set read_fds;


    //todo




    while (1) {
        pid_t pid = fork();
        char buff[100];
        int client_fd;

        if (pid == 0) {
            while (1) {
                client_fd = accept(fd, (struct sockaddr *)&addr, sizeof(struct sockaddr));
            }
            return 0;
        }

        while(1) {
            read(client_fd, buff, 100);
            printf("Message from client \'%s'\\n");
        }
    }

    shutdown(fd, SHUT_RDWR);
    close(fd);

    return 0;
}