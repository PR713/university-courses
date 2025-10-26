#include <stdio.h>
#include <signal.h>

void hello() {
    printf("Ja cie ale sygnal :O\n");
}

int main() {

    signal(SIGUSR1, hello);
    raise(SIGUSR1);

    return 0;
}