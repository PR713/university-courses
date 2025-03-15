#include <stdio.h>

int collatz_cojnecture(int input) {
    if (input % 2 == 0) {
        return input / 2;
    } else {
        return 3 * input + 1;
    }
}


int test_collatz_convergence(int input, int max_iter, int *steps) {

    int resultInput = input;

    for (int step = 0; step < max_iter; step++) {
        resultInput = collatz_cojnecture(resultInput);
        steps[step] = resultInput;

        if (resultInput == 1) {
            return step;
        }
    }

    return 0;
}