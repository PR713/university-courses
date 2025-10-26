#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() {

    int fd;
    fd = open("potok", O_RDONLY);
    char napis[20];
    read(fd, &napis, 20);
    printf("%s", napis);
    close(fd);
    return 0;
}
