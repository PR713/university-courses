#define _POSIX_C_SOURCE 200112L
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

volatile sig_atomic_t request_count = 0;
pid_t sender_pid = 0;
volatile sig_atomic_t mode = 0;
pid_t counting_pid = 0;

void start_counting_process() {
    if (counting_pid != 0) {
        //proces potomny już sobie liczy :)
        return;
    }

    counting_pid = fork();
    //jeśli nie zrobimy forka to handler zablokuje program i while(mode==2) nie przerywał
    //się nigdy bo program siedział w pętli w nieskończoność nawet jeśli były wysyłane inne 
    //tryby i nie odbierał ich, oczekiwały one ale nigdy nie zostałyby odebrane
    //teraz możemy nawet odsyłać sobie non stop sygnału tak o..

    if (counting_pid == 0) {
        // proces potomny
        int counter = 1;
        while (1) {
            printf("%d\n", counter++);
            sleep(1);
        }

        exit(0); // niby nieosiągalne, ale ładnie wygląda
    }
}


void stop_counting_process() {
    if (counting_pid != 0) {
        kill(counting_pid, SIGTERM);
        waitpid(counting_pid, NULL, 0);
        counting_pid = 0; //z powrotem 
    }
}


void ctrlc_message(int sig) {
    printf("Wciśnięto CTRL+C\n");
}



void handler(int sig, siginfo_t *info){
    sender_pid = info->si_pid;
    printf("Otrzymano sygnał SIGUSR1 od PID: %d\n", sender_pid);
    request_count++; //jeśli zmiana trybu to prev != curr no to if dodatkowy
    mode = info->si_value.sival_int;
    
    switch(mode) {
        case 1:
            printf("Otrzymano %d żądań zmiany trybu.\n", request_count);
            break;
        case 2:
            start_counting_process();
            break;
        case 3:
            signal(SIGINT, SIG_IGN);
            //printf("Ignoruję Ctrl+c\n");
            break;
        case 4:
            signal(SIGINT, ctrlc_message);
            break;
        case 5:
            printf("Zamykam catcher\n");
            exit(0);
    }

    if (mode != 2) {
        stop_counting_process();
    }
    
    //kill(sender_pid, SIGUSR1); //też można bo senderowi val niepotrzebny więc 
    //i tak jest default śmieciowa wartość.. + nie wysyłamy sygnałów z powrotem w inf
    union sigval val;
    sigqueue(sender_pid, SIGUSR1, val);
}



int main(int argc, char *argv[]){

    struct sigaction sa;

    sa.sa_sigaction = handler; //zamiast sa.sa_handler, dzięki temu przekazujemy więcej info
    sa.sa_flags = SA_SIGINFO; //uzyskujemy info o nadawcy
    sigemptyset(&sa.sa_mask);
    sigaction(SIGUSR1, &sa, NULL);

    sigset_t mask, oldmask;
    sigemptyset(&mask);
    sigaddset(&mask, SIGUSR1);
    sigprocmask(SIG_BLOCK, &mask, &oldmask);

    printf("Catcher PID: %d\n", getpid());

    while(1) {
        sigsuspend(&oldmask);
    }   

    sigprocmask(SIG_UNBLOCK, &mask, NULL);

    return 0;

}