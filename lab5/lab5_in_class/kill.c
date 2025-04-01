#include <stdio.h>
#include <signal.h>
#include <sys/types.h>

//kill i raise, raise czeka, kill wysyła na pid programu
// o nazwie kill sygnał SIGUSER1

int main(int argc, int *argv[]) {
    if (argc != 2) {
        return -1;
    }


    pid_t pid = (pid_t) atoi(argv[1]);
    kill(pid, SIGUSR1);
    return 0;
}