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

int main(int argc, char *argv[]) {

    if (argc != 4) {
        perror("Incorrect number of arguments provided");
        return 1;
    }

    int fd = -1;
    if((fd=socket(AF_INET, SOCK_STREAM,0)) == -1){
        perror("Error creating socket");
    }

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = atoi(argv[3]);
    addr.sin_addr.s_addr = inet_addr(argv[2]);
    
    if(connect(fd, (struct sockaddr *)&addr, sizeof(struct sockaddr)) == -1) {
        perror("Error connecting to server");
    }

    char buff[20];
    int to_send = sprintf(buff, "HELLO from: %zu", getpid());

    if (write(fd, buff, to_send + 1) == -1) {
        perror("Error sending msg to server");
    }

    
    while (1) {
        pid_t pid = fork();
        char buff[100];

        if (pid == 0) {
            while (1) {
                fgets("Enter a message: %s", buff, STDIN_FILENO);
                write(fd, buff, 100);
            }
            return 0;
        }

        while(1) {
            read(fd, buff, 100);
            printf("Message from other client \'%s'\\n");
        }
    }

    shutdown(fd, SHUT_RDWR);
    close(fd);

    return 0;
}