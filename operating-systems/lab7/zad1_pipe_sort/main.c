#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

// Zadanie:
// Uzupelnij program tak, aby za pomoca fork() i execlp()
// uruchomic polecenie 'sort' w procesie potomnym.
// Proces rodzica ma przeslac dane do potomka za pomoca potoku.
// Tak aby poprawne bylo wywolanie
//
//     write(fd[1], "ccc\nbbb\naaa\n", 12);
//
// Z Wynikiem:
//     aaa
//     bbb
//     ccc

int main() {
    int fd[2];
    pipe(fd);

    pid_t pid = fork();

    if (pid == 0) {
        close(fd[1]);
        char buf[20];
        read(fd[0], buf, 20);
        execlp("sort", "sort", buf ,NULL);
    } else {
        close(fd[0]);
        write(fd[1], "ccc\nbbb\naaa\n", 12);
    }

    close(fd[1]);
    close(fd[0]);

    return 0;
}
