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

typedef enum {
    CMD_LIST,
    CMD_TOALL,
    CMD_TOONE,
    CMD_STOP,
    CMD_INVALID
} CommandType;


struct client_info {
    const char* clients_fds[10];
    int id[10];
    char date[20];
} client_info;


int main() {

    int fd = -1;
    if ((fd = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Error creating socket");
    }

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = 65432;
    addr.sin_addr.s_addr = inet_addr("127.0.0.5");

    if (bind(fd, (struct sockaddr *)&addr, sizeof(struct sockaddr)) == -1) {
        perror("Error binding");
    }

    listen(fd, 4);

    while (1) {
        pid_t pid = fork();
        char buff[100];

        if (pid == 0) {
            while (1) {
                int client_fd = accept(fd, (struct sockaddr *)&addr, sizeof(struct sockaddr));
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