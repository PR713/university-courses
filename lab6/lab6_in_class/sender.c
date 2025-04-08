#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() {
    int fd;

    fd = open("potok", O_WRONLY);
    write(fd, "Helloworld\n", 12);
    
    return 0;
}