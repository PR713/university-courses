#define _POSIX_C_SOURCE 200112L
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

volatile sig_atomic_t confirmed = 0;
pid_t catcher_pid = 0;

void handle_confirmation(int sig, siginfo_t *info){
    // catcher_pid = info->si_pid;
    // confirmed++;
    // printf("Potwierdzenie nr %d odebrania SIGUSR1 od PID: %d\n", confirmed, catcher_pid);
    // kill(catcher_pid, SIGUSR1); //nie mają cały czas do siebie wysyłać sygnałów w inf więc tylko:
    confirmed = 1;
}


int main(int argc, char *argv[]){

    if (argc != 3){
        return -1;
    }

    pid_t catcher_pid = atoi(argv[1]);
    int mode = atoi(argv[2]);
    
    if (mode < 1 || mode > 5) {
        fprintf(stderr, "Niepoprawny tryb: %d\n", mode);
        return 1;
    }

    struct sigaction sa;

    sa.sa_handler = handle_confirmation;
    sa.sa_flags = 0;
    sigemptyset(&sa.sa_mask);
    sigaction(SIGUSR1, &sa, NULL);


    sigset_t mask, oldmask;
    sigemptyset(&mask);
    sigaddset(&mask, SIGUSR1);
    sigprocmask(SIG_BLOCK, &mask, &oldmask);

    union sigval val;
    val.sival_int = mode;
    sigqueue(catcher_pid, SIGUSR1, val);

    if (mode == 5) {
        return 0;
    }
    while(!confirmed){
        sigsuspend(&oldmask);
    }

    sigprocmask(SIG_UNBLOCK, &mask, NULL);

    return 0;
}