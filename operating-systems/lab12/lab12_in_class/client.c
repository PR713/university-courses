//SOCK_DATAGRAM
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

int main() {
    int fd = -1;
    if((fd=socket(AF_UNIX, SOCK_DGRAM,0)) == -1){
        perror("Error creating socket");
    }

    struct sockaddr_un addr;
    addr.sun_family = AF_UNIX;
    strcpy(addr.sun_path, "\0");
    if(connect(fd, (struct sockaddr *)&addr, sizeof(struct sockaddr)) == -1) {
        perror("Error connecting to server");
    }

    char buff[20];
    int to_send = sprintf(buff, "HELLO from: %zu", getpid());

    if (write(fd, buff, to_send + 1) == -1) {
        perror("Error sending msg to server");
    }

    shutdown(fd, SHUT_RDWR);
    close(fd);

    return 0;
}