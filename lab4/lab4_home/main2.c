#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int global = 0;

int main(int argc, char *argv[]){
    //example: ./main2 . <- child exit code 0
    // ./main2 abc <- child exit code 2
    // ./main2 -l <- child exit code 0
    if (argc != 2){
        printf("Incorrect number of arguments!");
        return EXIT_FAILURE;
    }

    int local = 0;

    printf("Name of program: %s\n", argv[0]);

    pid_t pid = fork(); //the child process gets copies of the variables local&global...

    if (pid < 0) {
        perror("fork() error");
        return EXIT_FAILURE;
    } else if (pid == 0) {
        printf("Child process..\n");
        local++;
        global++;
        printf("Child pid = %d, parent pid = %d\n", getpid(), getppid());
        printf("Child's local = %d, child's global = %d\n", local, global);
        execl("/bin/ls", "ls", argv[1], NULL);
        perror("Błąd execl()\n");
        exit(EXIT_FAILURE);
    } else {
        printf("Parent process..\n");
        printf("parent pid = %d, child pid = %d\n", getpid(), pid); 
        
        int status;
        waitpid(pid, &status, 0);

        if (WIFEXITED(status)) {
            printf("Child exit code: %d\n", WEXITSTATUS(status));
        } else {
            printf("Child did not exit normally.\n");
        }

        printf("Parent's local = %d, parent's global = %d\n", local, global);
    }
    // if the child process finishes before the parent process, then it has a zombie status,
    // and still waitpid/wait functions are working properly... else the parent is waiting for
    // its child process, the case when parent is finishing beforce the child, that can't occurre
    // because we use waitpid/wait function

    return EXIT_SUCCESS;
}