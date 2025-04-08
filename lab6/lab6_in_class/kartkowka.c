#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>


int main() {

    int fd[2];
    pipe(fd);

    if (fork() == 0) {
        close(fd[1]);
        //sleep(1); <- naprawia oczekiwanie
        char c;
        while(read(fd[0], &c, 1) > 0)
            printf("%c", c);
        printf("END\n"); //\n potem możemy pisać w konsoli
    } else {
        close(fd[0]);
        write(fd[1], "ABC", 3);
        //close(fd[1]);
    }

    return 0;
}