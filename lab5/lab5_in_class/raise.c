#include <stdio.h>
#include <signal.h>

void hello() {
    printf("Sygnal obsluzony\n");
}

int main() {

    signal(SIGUSR1, hello);
    printf("Moje pid %d\n", getpid());
    pause();
    return 0;
}