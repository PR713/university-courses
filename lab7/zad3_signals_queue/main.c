#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <signal.h>
#include <errno.h>
#include <limits.h>

// Zadanie:
// Proces potomny powinien obsluzyc sygnaly SIGUSR1 i SIGUSR2
// i wypisac otrzymana wraz z nimi wartosc (int).
// Rodzic powinien przeslac wartosc(argv[1]) za pomocą sygnalu (argv[2]).
// Jeśli sygnac nie zostanie obsluzony w ciagu 1 sekundy,
// proces potomny ma zostac zakończony.

void handler(int sig, siginfo_t *si, void *unused) {
    int value = si->si_value.sival_int;
    printf("Received value %d with signal.\n", value);
    //brakło czasu ale pomysł żeby tutaj wysłać kill na jakiś sygnał a w procesie
    //macierzystym ustawić setprocmask i sigset_t set tak żeby tylko na ten sygnał reagowało
    //'jako potwierdzenie obsłużenia' wraz z clock_t time = clock();
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        return 1;
    }

    pid_t pid = fork();

    if (pid == 0) {
        struct sigaction sa;
        sa.sa_sigaction = handler;
        sa.sa_flags = SA_SIGINFO;
        sigaction(SIGUSR1, &sa, NULL);
        sigaction(SIGUSR2, &sa, NULL);

        while (1) {
            pause();
        }
    } else {
        char *endptr;
        union sigval val;
        val.sival_int = strtol(argv[1], &endptr, 10);
        errno = 0;
        if ((errno == ERANGE && (val.sival_int == LONG_MAX || val.sival_int == LONG_MIN))
            || (errno != 0 && val.sival_int == 0)) {
            perror("strtol");
            exit(EXIT_FAILURE);
        }
        if (endptr == argv[1]) {
            fprintf(stderr, "No digits were found\n");
            exit(EXIT_FAILURE);
        }
        //val.sival_int = atoi(argv[1]); // doesnt check possible non numeric value
        sigqueue(pid, atoi(argv[2]), val);
        sleep(1);
    }

    return 0;
}
