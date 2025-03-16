#include <stdio.h>
#include <dlfcn.h>
#include "collatzlibrary.h"

#ifdef DYNAMIC_LIB
    #define LIB_TYPE "Dynamic Library"
#else
    #define LIB_TYPE "Unknown Library"
#endif

int main() {

    printf("Using %s\n", LIB_TYPE);

    void *handle = dlopen("libsharedcollatzlibrary.so", RTLD_LAZY);
    if(!handle) {
        printf("There occured an error while loading the library!\n");
        return -1;
    }

    int (*test_collatz_conv) (int, int, int*);
    test_collatz_conv = (int (*)(int, int, int*))dlsym(handle,"test_collatz_convergence");

    if (dlerror() != NULL) {
        printf("There occured an error while finding the function!");
        dlclose(handle);
        return -1;
    }

    int numbers[] = {6, 1, 13, 19, 77, 125, 98};
    int max_iter = 50;
    int steps[max_iter];

    for (int i = 0; i < sizeof(numbers)/sizeof(numbers[0]); i++) {
        int input = numbers[i];

        if (input == 1){
            printf("Convergence in 0 steps: 1 \n");

        } else {
            int steps_count = test_collatz_conv(input, max_iter, steps);

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

    dlclose(handle);
    
    return 0;
}