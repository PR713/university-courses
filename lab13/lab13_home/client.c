//SOCK_DGRAM
//./client Radek 127.0.0.5 12345
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

void handle_exit(int sig) {
    write(sockfd, "STOP", 4);
    close(sockfd);
    printf("\nDisconnected.\n");
    exit(0);
}

void* receive_thread(void* arg) {
    char buffer[BUFFER_SIZE];
    while (1) {
        memset(buffer, 0, sizeof(buffer));
        int bytes = read(sockfd, buffer, sizeof(buffer));
        if (bytes <= 0) break;
        if (strncmp(buffer, "PING", 4) == 0) {
            write(sockfd, "ALIVE", 5);
        } else {
            printf("%s\n", buffer);
        }
    }
    return NULL;
}

int main(int argc, char *argv[]) {

    if (argc != 4) {
        perror("Incorrect number of arguments provided");
        return 1;
    }


    strncpy(username, argv[1], sizeof(username));
    const char *server_ip = argv[2];
    int port = atoi(argv[3]);

    signal(SIGINT, handle_exit);


    if((sockfd=socket(AF_INET, SOCK_DGRAM, 0)) == -1){
        perror("Error creating socket");
    }

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    addr.sin_addr.s_addr = inet_addr(argv[2]);
    
    if(connect(sockfd, (struct sockaddr *)&addr, sizeof(struct sockaddr)) == -1) {
        perror("Error connecting to server");
    }

    write(sockfd, username, strlen(username));

    pthread_t recv_thread;
    pthread_create(&recv_thread, NULL, receive_thread, NULL);

    char buffer[BUFFER_SIZE];
    while (1) {
        fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "\n")] = 0;
        if (strncmp(buffer, "STOP", 4) == 0) {
            handle_exit(0);
        }
        write(sockfd, buffer, strlen(buffer));
    }

    return 0;
}