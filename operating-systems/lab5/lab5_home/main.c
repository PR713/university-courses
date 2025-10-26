#define _POSIX_C_SOURCE 200112L
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>


void handler(int signum){
    printf("Otrzymano sygnał SIGUSR1\n");
}

int main(int argc, char *argv[]){

    if (argc != 2) {
        printf("Opcje dostępne <none|ignore|handler|mask>\n");
        return -1;
    }

    if (strcmp(argv[1], "none") == 0){
        signal(SIGUSR1, SIG_DFL);

    } else if (strcmp(argv[1], "ignore") == 0){
        signal(SIGUSR1, SIG_IGN);

    } else if (strcmp(argv[1], "handler") == 0){
        signal(SIGUSR1, handler);

    } else if (strcmp(argv[1], "mask") == 0) {
        sigset_t set;
        sigemptyset(&set);
        sigaddset(&set, SIGUSR1);
        sigprocmask(SIG_BLOCK, &set, NULL);

        raise(SIGUSR1);

        sigset_t pending;

        sigpending(&pending);

        if (sigismember(&pending, SIGUSR1)) {
            printf("SIGUSR1 jest w stanie oczekiwania\n");
        } else {
            printf("SIGUSR1 nie jest oczekujący\n");
        }

    } else {
        printf("Nieznane polecenie.");
    }

    raise(SIGUSR1);


    return 0;

}