#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

const double START = 0.0;
const double END = 1.0;

struct arg_for_thread_function {
    int from;
    int to;
    double step;
    double *result;
    int id;
};

double function(double x){
    return 4.0/(x*x + 1.0);
}

void* thread_function(void* args){
    struct arg_for_thread_function* arg = (struct arg_for_thread_function*) args;
    int from = arg->from;
    int to = arg->to;
    double step = arg->step;

    double partial_sum = 0.0;

    for (int i = from; i < to; i++) {
        partial_sum += function(START + i * step) * step; //if there were (i+1), that would be the right rectangles method,
        //but now is left rectangles :D
    }

    *(arg->result) = partial_sum;

    return NULL;
}



int main(int argc, char *argv[]){
    if (argc != 3) {
        fprintf(stderr, "Usage: %s step n \n", argv[0]);
        return -1;
    }

    double step = atof(argv[1]);
    int n = atoi(argv[2]);
    int num_of_intervals = (int) ((END - START) / step);

    for (int k = 1; k <= n; k++){
        pthread_t tids[k];
        double results[k];

        struct arg_for_thread_function args[k];

        clock_t start_time = clock();

        for (int i = 0; i < k; i++){ 
            int from = i * num_of_intervals / k;
            int to = (i + 1) * num_of_intervals / k;

            args[i].from = from;
            args[i].to = to;
            args[i].step = step;
            args[i].result = &results[i];
            args[i].id = i;
            
            pthread_create(&tids[i], NULL, thread_function, &args[i]);
        }

        for (int i = 0; i < k; i++) {
            pthread_join(tids[i], NULL);
        }

        double total_sum = 0.0;

        for (int i = 0; i < k; i++) {
            total_sum += results[i];
        }

        clock_t end_time = clock();

        double elapsed = (double)(end_time - start_time) / CLOCKS_PER_SEC;

        printf("Threads: %d, result: %.12f, time %.5f\n", k, total_sum, elapsed);
    }


    return 0;
}