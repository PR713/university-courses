#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(){

    int n = 10;

    for (int i = 0; i < n; i++){
    
        pid_t child_pid = fork();
        printf("%d\n", child_pid);

        if (child_pid == 0) {
            printf("Hello tu process PID: %d\n", (int)getpid());
            _exit(0); //_exit zamyka systemowo trzeba \n jeśli exit(0) to kompilatorowo
            // to bez \n git
        }
    }

    return 0;
}