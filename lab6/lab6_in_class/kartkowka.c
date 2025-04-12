#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>


int main() {

    int fd[2];
    pipe(fd);

    if (fork() == 0) {
        close(fd[1]);
        sleep(1);
        char c;
        while(read(fd[0], &c, 1) > 0)
            printf("%c\n", c);
        printf("END\n"); //\n potem możemy pisać w konsoli
        //jeśli nic nie ma to zasypia (blokuje się), jeśli coś jest to czyta i dopóki
        //są pisarze to czeka na więcej
    } else {
        close(fd[0]);
        write(fd[1], "ABC", 3);
        //close(fd[1]);
        sleep(5);
        //printuje się END mimo że close(fd[1]) zakomentowane bo rodzic po prostu robi return 0 i deskryptory
        //same się zamykają, jak damy sleep(5) to mamy A B C i dopiero po 5 sekundach END
    }

    return 0;
}