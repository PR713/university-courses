//SOCK_DGRAM
//./client Radek 127.0.0.1 12345
// ^^^ip serwera, który działa na wszystkich IP o porcie 12345
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <pthread.h>

#define BUFFER_SIZE 256

int sockfd;
char username[32];
struct sockaddr_in server_addr;
socklen_t server_len;

void handle_exit(int sig) {
    sendto(sockfd, "STOP", 4, 0, (struct sockaddr*)&server_addr, server_len);
    close(sockfd);
    printf("\nDisconnected.\n");
    exit(0);
}

void* receive_thread(void* arg) {
    char buffer[BUFFER_SIZE];
    struct sockaddr_in from_addr;
    socklen_t from_len = sizeof(from_addr);
    
    while (1) {
        memset(buffer, 0, sizeof(buffer));
        ssize_t bytes = recvfrom(sockfd, buffer, sizeof(buffer) - 1, 0,
                                 (struct sockaddr*)&from_addr, &from_len);
        if (bytes > 0) {
            buffer[bytes] = '\0';
            if (strncmp(buffer, "PING", 4) == 0) {
                sendto(sockfd, "ALIVE", 5, 0, (struct sockaddr*)&server_addr, server_len);
            } else if (strncmp(buffer, "CONNECTED", 9) == 0) {
                printf("Successfully connected to server!\n");
                printf("Available commands:\n");
                printf("  LIST - show all active clients\n");
                printf("  2ALL <message> - send message to all clients\n");
                printf("  2ONE <name> <message> - send private message\n");
                printf("  STOP - disconnect from server\n");
                printf("Enter command: ");
                fflush(stdout);
            } else {
                printf("%s\n", buffer);
                printf("Enter command: ");
                fflush(stdout);
            }
        }
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s <username> <server_ip> <port>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    strncpy(username, argv[1], sizeof(username) - 1);
    username[sizeof(username) - 1] = '\0';
    const char *server_ip = argv[2];
    int port = atoi(argv[3]);

    signal(SIGINT, handle_exit);

    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) == -1) {
        perror("Error creating socket");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = inet_addr(server_ip);
    server_len = sizeof(server_addr);

    //pierwszy komunikat (rejestracja)
    sendto(sockfd, username, strlen(username), 0, 
           (struct sockaddr*)&server_addr, server_len);

    pthread_t recv_thread;
    pthread_create(&recv_thread, NULL, receive_thread, NULL);

    printf("Connecting to server %s:%d as '%s'...\n", server_ip, port, username);

    char buffer[BUFFER_SIZE];
    while (1) {
        if (fgets(buffer, sizeof(buffer), stdin) == NULL) {
            break;
        }
        
        buffer[strcspn(buffer, "\n")] = 0;
        
        if (strlen(buffer) == 0) {
            continue;
        }
        
        if (strncmp(buffer, "STOP", 4) == 0) {
            handle_exit(0);
        }
        
        sendto(sockfd, buffer, strlen(buffer), 0, 
               (struct sockaddr*)&server_addr, server_len);
    }

    handle_exit(0);
    return 0;
}