#include <stdio.h>
#include <signal.h>
#include <sys/types.h>


int cntReceived = 0; 

void handleSignal() {
    cntReceived++;
    printf("Number of received signals %d\n", cntReceived);
}

int main() {
    
    pid_t pid = fork();
    int cnt = 0;

    if (pid == 0){
        signal(SIGUSR1, handleSignal);
        while (1) pause();
    } else {
        while(1) {
            cnt += 1;
            printf("Liczba sygnalow wyslanych %d\n ", cnt);
            kill(pid, SIGUSR1);
            
        }
    }
    
    return 0;
}

//to do wyświetlić stosunek received/send z użyciej sigqueue można przekazać dodatkową
// wartośc wraz z wysłaniem