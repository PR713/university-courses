#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(){

    int n = 5;
    int counter = 0;

    for (int i = 0; i < n; i++){
        counter++;
        pid_t child_pid = fork();

        if (child_pid == 0) {
            printf("Hello tu process PID: %d\n", (int)getpid());
            char * const av[] = {"ls", "-l", NULL};
            execv("/bin/ls", av);
        }
    }
    printf("%d\n", counter);
    exit(1);
}