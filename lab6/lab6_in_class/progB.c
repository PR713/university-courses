#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char *argv[]) {

    char modified[] = argv[1];
    modified[0] = 'g';
 
    return modified;
}
// (: main zwraca int a nie char[]