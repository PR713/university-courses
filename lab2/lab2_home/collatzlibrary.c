#include <stdio.h>

int collatz_cojnecture(int input) {
    if (input % 2 == 0) {
        return input / 2;
    } else {
        return 3 * input + 1;
    }
}


int test_collatz_convergence(int input, int max_iter, int *steps) {

    if (input == 1) {
        return 0;
    }

    int result_input = input;

    for (int step = 1; step <= max_iter; step++) {
        result_input = collatz_cojnecture(result_input);
        steps[step - 1] = result_input;

        if (result_input == 1) {
            return step;
        }
    }

    return 0;
}