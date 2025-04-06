#define _POSIX_C_SOURCE 200112L
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

pid_t sender_pid = 0;

void handler(int sig, siginfo_t *info){
    sender_pid = info->si_pid;
    printf("Otrzymano sygnał SIGUSR1 od PID: %d\n", sender_pid);
    kill(sender_pid, SIGUSR1);
}

int main(int argc, char *argv[]){

    struct sigaction sa;

    sa.sa_sigaction = handler; //zamiast sa.sa_handler, dzięki temu przekazujemy więcej info
    sa.sa_flags = SA_SIGINFO; //uzyskujemy info o nadawcy
    sigemptyset(&sa.sa_mask);
    sigaction(SIGUSR1, &sa, NULL);

    printf("Catcher PID: %d\n", getpid());

    while(1) {
        pause();
    }   

    return 0;

}