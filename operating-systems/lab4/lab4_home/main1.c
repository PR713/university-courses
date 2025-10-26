#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

    if (argc != 2) {
        printf("Incorrect number of arguments!");
        return EXIT_FAILURE;
    }

    int n = atoi(argv[1]);

    for (int i = 0; i < n; i++) {

        pid_t child_pid = fork();
        if (child_pid < 0) {
            perror("fork() error");
        }

        if (child_pid == 0) {
            printf("%d %d\n", getppid(), getpid());
            _exit(0);
        }
    }
    
    for (int i = 0; i < n; i++) {
        wait(NULL); // we wait n times for child processes :)
    } //to ensure we print below message as the last one, not in 
    //the different positions

    printf("Number of processes: %d\n", n);
    return 0;
}
