#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(void) {
    srand(time(NULL));      //      use time in seconds to set seed

    //      rand() returns a pseudo-random integer between 0 and RAND_MAX

    /* Print 5 random numbers from 0 to 99 */
    for (int i = 0; i < 5; i++) {
        printf("%d ", rand() % 100);
    }
    printf("\n");

    return 0;
}