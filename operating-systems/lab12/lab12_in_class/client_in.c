//SOCK_DATAGRAM
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define ADDRESS = "127.0.0.1"

int main() {
    int fd = -1;
    if((fd=socket(AF_INET, SOCK_DGRAM,0)) == -1){
        perror("Error creating socket");
    }

    struct sockaddr_in addr;
    struct in_addr in_address;
    addr.sin_family = AF_INET;
    addr.sin_port = 65432;
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    //strcpy(addr.sun_path, "\0");
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