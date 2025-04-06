#define _POSIX_C_SOURCE 200112L
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

int received_confirmation = 0;

pid_t sender_pid = 0;

void handle_confirmation(int sig, siginfo_t *info){
    sender_pid = info->si_pid;
    received_confirmation++;
    printf("Potwierdzenie nr %d odebrania SIGUSR1 od PID: %d\n", received_confirmation, sender_pid);
    kill(sender_pid, SIGUSR1);
}


int main(int argc, char *argv[]){

    if (argc != 2){
        return -1;
    }

    kill(atoi(argv[1]), SIGUSR1);


    struct sigaction sa;

    sa.sa_sigaction = handle_confirmation;
    sa.sa_flags = SA_SIGINFO;
    sigemptyset(&sa.sa_mask);
    sigaction(SIGUSR1, &sa, NULL);

    while(1){
        pause();
    }//TODO tutaj bezpieczne oczekiwania z pomocą sigsuspend lepiej

    return 0;
}