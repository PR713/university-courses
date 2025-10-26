#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/stat.h>

// Zadanie:
// Utworz proces potomny.
// Potomek ma wypisac:
//     [POTOMEK] PID: ..., PPID: ...
// i zakonczyc sie z kodem 42.
// Rodzic powinien:
//     - poczekac na zakonczenie potomka,
//     - wypisac:
//     [RODZIC] PID: ..., otrzymal status zakonczenia: ...

int main() {

    pid_t pid = fork();

    if (pid == 0) {
        printf("[POTOMEK] PID: %d, PPID: %d\n", getpid(), getppid());
        exit(42);
    } else {
        int statloc;
        wait(&statloc);
        printf("[RODZIC] PID: %d, otrzymal status zakonczenia: %d\n", getpid(), WEXITSTATUS(statloc));

    }

    return 0;
}