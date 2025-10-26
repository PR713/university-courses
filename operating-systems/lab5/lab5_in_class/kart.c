#include <stdio.h>
#include <signal.h>



int main() {
    signal(SIGUSR1, SIG_IGN);
    raise(SIGUSR1);
    raise(SIGUSR2);
    printf("Po sygnalach\n");
}