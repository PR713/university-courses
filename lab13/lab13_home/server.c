//SOCK_DGRAM
//./server 12345
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
#include <sys/time.h>
#include <fcntl.h>
#include <pthread.h>

#define MAX_CLIENTS 10
#define MAX_NAME 32
#define BUFFER_SIZE 256
#define ALIVE_INTERVAL 10

typedef struct {
    char name[MAX_NAME];
    struct sockaddr_in client_addr;
    time_t last_alive;
} Client;

Client clients[MAX_CLIENTS] = {0};

int server_socket;

void broadcast_message(const char *msg, struct sockaddr_in exclude_addr) {
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (&clients[i].client_addr != NULL && &clients[i].client_addr != &exclude_addr) {
            sendto(server_socket, msg, NULL, (struct sockaddr*)&clients[i].client_addr, sizeof(struct sockaddr*));
        }
    }
}


void remove_client(int i) { //usunąć sockfd wszędzie i usuwać po prostu clientów na podstawie ip i portu
    close(clients[i].sockfd);
    printf("Client '%s' disconnected.\n", clients[i].name);
    clients[i].sockfd = 0;
    clients[i].name[0] = '\0';
}


void handle_client(int i) {
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
    } else if (strncmp(buffer, "2ALL", 4) == 0) {
        char msg[BUFFER_SIZE];
        snprintf(msg, sizeof(msg), "[%s] %s", clients[i].name, buffer + 5);
        broadcast_message(msg, clients[i].sockfd);
    } else if (strncmp(buffer, "2ONE", 4) == 0) {
        char target[MAX_NAME];
        sscanf(buffer + 5, "%s", target); //%s czyta jeden wyraz (do białego znaku np ' ')
        char *msg_start = strchr(buffer + 5, ' '); //szuka pierwsze wystąpienie ' ' od 5. indeksu
        //np 2ONE Radek treść, R to 5 indeks
        if (!msg_start) return;
        msg_start++; //od znalezionej spacji znak w przód

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
    socklen_t server_len = sizeof(server_addr);

    server_socket = -1;
    if ((server_socket = socket(AF_INET, SOCK_DGRAM, 0)) == -1) {
        perror("Error creating socket");
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.5");

    if (bind(server_socket, (struct sockaddr *)&server_addr, &server_len) == -1) {
        perror("Error binding");
    }

    printf("Server started on port %d\n", port);

    fd_set read_fds;

    pthread_t recv_thread;
    pthread_create(&recv_thread, NULL, handle_client, NULL);
    
    while (1) {
        

        // Ping & remove inactive clients
        time_t now = time(NULL);
        for (int i = 0; i < MAX_CLIENTS; i++) {
            if (clients[i].sockfd > 0 && now - clients[i].last_alive > ALIVE_INTERVAL) {
                write(clients[i].sockfd, "PING", 4);
                clients[i].last_alive = now - ALIVE_INTERVAL / 2;
            }
        }
    }


    return 0;
}