//SOCK_STREAM
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <signal.h>

#define BUFFER_SIZE 256
int sockfd = -1;
char username[32];

void handle_exit(int sig) {
    write(sockfd, "STOP", 4);
    close(sockfd);
    printf("\nDisconnected.\n");
    exit(0);
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


    if((sockfd=socket(AF_INET, SOCK_STREAM,0)) == -1){
        perror("Error creating socket");
    }

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = atoi(argv[3]);
    addr.sin_addr.s_addr = inet_addr(argv[2]);
    
    if(connect(sockfd, (struct sockaddr *)&addr, sizeof(struct sockaddr)) == -1) {
        perror("Error connecting to server");
    }


    char buff[20];
    int to_send = sprintf(buff, "HELLO from: %zu", getpid());

    if (write(sockfd, buff, to_send + 1) == -1) {
        perror("Error sending msg to server");
    }

    signal(SIGINT, handle_exit);
    
    while (1) {
        pid_t pid = fork();
        char buff[100];

        if (pid == 0) {
            while (1) {
                fgets("Enter a message: %s", buff, STDIN_FILENO);
                write(sockfd, buff, 100);
            }
            return 0;
        }

        while(1) {
            read(sockfd, buff, 100);
            printf("Message from other client \'%s'\\n");
        }
    }

    shutdown(sockfd, SHUT_RDWR);
    close(sockfd);

    return 0;
}