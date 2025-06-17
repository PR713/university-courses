#include <stdio.h>



int main(){

    int x = 6;  // 00000110
    int y = 12; // 00001100
    int z = 0;  // 00000000

    z = x & y;  // 00000100 AND

    printf("%d \n", z);

    z = x | y;  // 00001110 OR

    printf("%d \n", z);

    z = x ^ y;  // 00001010 XOR ~(p <=> q)
    printf("%d\n ", z);

    z = x << 1; // 00001100 LEFT SHIFT
    z = x >> 2; // 00000001 RIGHT SHIFT

    return 0;
}