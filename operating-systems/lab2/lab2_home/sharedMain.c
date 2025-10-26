#include <stdio.h>


int main() {

    int numbers[] = {6, 1, 13, 19, 77, 125, 98};
    int max_iter = 50;
    int steps[max_iter];

    for (int i = 0; i < sizeof(numbers)/sizeof(numbers[0]); i++) {
        int input = numbers[i];

        if (input == 1){
            printf("Convergence in 0 steps: 1 \n");

        } else {
            int steps_count = test_collatz_convergence(input, max_iter, steps);

            if (steps_count == 0) {
                printf("Failure to converge to 1 in required number of iterations: %d \n", max_iter);

            } else {
                printf("Convergence in %d steps: ", steps_count);
                printf("%d -> ", input);

                for (int j = 0; j < steps_count - 1; j++){
                    printf("%d%s", steps[j], (j == steps_count - 2) ? " -> 1 \n" : " -> " );
                }
            }
        }
    }
    
    return 0;
}