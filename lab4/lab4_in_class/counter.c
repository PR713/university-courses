#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(){

    int n = 10;
    int counter = 0;

    for (int i = 0; i < n; i++){
    
        pid_t child_pid = vfork();

        if (child_pid == 0) {
            printf("Hello tu process PID: %d\n", (int)getpid());
            counter++;
            //exit(1);
        }
    }

    printf("%d\n", counter);
    exit(1);
}// i jest wspólne w pętli (vfork współdzieli, tak samo counter) i każdy poprzedni blokowany i jak ostatni zrobi całą pętle
//to mamy print counter
//counter można też przed vfork bo blokowane są