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

void broadcast_message(const char *msg, int exclude_fd) {
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].sockfd > 0 && clients[i].sockfd != exclude_fd) {
            write(clients[i].sockfd, msg, strlen(msg));
        }
    }
}


void remove_client(int i) {
    close(clients[i].sockfd);
    printf("Client '%s' disconnected.\n", clients[i].name);
    clients[i].sockfd = 0;
    clients[i].name[0] = '\0';
}


void handle_client_message(int i) {
    char buffer[BUFFER_SIZE] = {0};
    int bytes = read(clients[i].sockfd, buffer, sizeof(buffer));
    if (bytes <= 0) {
        remove_client(i);
        return;
    }

    if (strncmp(buffer, "LIST", 4) == 0) {
        char list[BUFFER_SIZE] = "Clients:\n";
        for (int j = 0; j < MAX_CLIENTS; j++) {
            if (clients[j].sockfd > 0) {
                strcat(list, clients[j].name);
                strcat(list, "\n");
            }
        }
        write(clients[i].sockfd, list, strlen(list));
    } else if (strncmp(buffer, "2ALL", 5) == 0) {
        char msg[BUFFER_SIZE];
        snprintf(msg, sizeof(msg), "[%s] %s", clients[i].name, buffer + 5);
        broadcast_message(msg, clients[i].sockfd);
    } else if (strncmp(buffer, "2ONE", 5) == 0) {
        char target[MAX_NAME];
        sscanf(buffer + 5, "%s", target);
        char *msg_start = strchr(buffer + 5, ' ');
        if (!msg_start) return;
        msg_start++;

        char msg[BUFFER_SIZE];
        snprintf(msg, sizeof(msg), "[%s -> %s] %s", clients[i].name, target, msg_start);

        for (int j = 0; j < MAX_CLIENTS; j++) {
            if (clients[j].sockfd > 0 && strcmp(clients[j].name, target) == 0) {
                write(clients[j].sockfd, msg, strlen(msg));
                break;
            }
        }
    } else if (strncmp(buffer, "STOP", 4) == 0) {
        remove_client(i);
    } else if (strncmp(buffer, "ALIVE", 5) == 0) {
        clients[i].last_alive = time(NULL);
    }
}

void signal_handler(int sig) {
    close(server_socket);
    printf("\nServer shutdown.\n");
    exit(0);
}



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


    while (1) {
        FD_ZERO(&read_fds);
        FD_SET(server_socket, &read_fds);
        int max_fd = server_socket;

        for (int i = 0; i < MAX_CLIENTS; i++) {
            if (clients[i].sockfd > 0) {
                FD_SET(clients[i].sockfd, &read_fds);
                if (clients[i].sockfd > max_fd) max_fd = clients[i].sockfd;
            }
        }
    }


    return 0;
}