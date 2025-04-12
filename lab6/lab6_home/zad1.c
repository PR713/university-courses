#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <time.h>
#include <stdlib.h>

double function(double x){
    return 4.0/(x*x + 1.0);
}

int main(int argc, char *argv[]){

    if (argc != 3){
        return -1;
    }

    double start = 0.0;
    double end = 1.0;
    double step = atof(argv[1]);
    int n = atoi(argv[2]);
    int num_of_intervals = (int) ((end - start) / step);

    for(int k = 1; k <= n; k++){
        int pipes[k][2]; //fd's
        pid_t pids[k];
        
        clock_t start_time = clock();

        for(int i = 0; i < k; i++){
            if (pipe(pipes[i]) == -1) {
                perror("pipe");
                return 1;
            }

            pids[i] = fork();

            if (pids[i] == -1){
                perror("fork");
                return 1;
            }

            if (pids[i] == 0){
                close(pipes[i][0]); //close read
                
                int from = i * num_of_intervals / k;
                int to = (i + 1) * num_of_intervals / k;

                double partial_sum = 0.0;

                for(int j = from; j < to; j++){
                    partial_sum += function(start + j * step) * step;
                }

                write(pipes[i][1], &partial_sum, sizeof(double));
                close(pipes[i][1]);
                exit(0);
            }

            close(pipes[i][1]);
        }

        double total_sum = 0.0;

        for (int i = 0; i < k; i++){
            double partial_s;
            read(pipes[i][0], &partial_s, sizeof(double));
            close(pipes[i][0]);
            total_sum += partial_s;
        }

        for (int i = 0; i < k; i++){
            wait(NULL);
        }

        clock_t end_time = clock();

        double elapsed = (double)(end_time - start_time) / CLOCKS_PER_SEC;

        printf("Processes: %d, result: %.12f, time %.5f\n", k, total_sum, elapsed);
    }

    return 0;
}