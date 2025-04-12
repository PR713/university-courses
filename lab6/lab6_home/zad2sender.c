#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>


int main(int argc, char *argv[]){
    if(argc != 4){
        return 1;
    }

    double start = atof(argv[1]); // !!!#include <stdlib.h>!!!
    double end = atof(argv[2]);
    double step = atof(argv[3]);

    int fd_out = open("potok1", O_WRONLY);
    int fd_in = open("potok2", O_RDONLY);

    write(fd_out, &start, sizeof(double));
    write(fd_out, &end, sizeof(double));
    write(fd_out, &step, sizeof(double));

    double result;

    read(fd_in, &result, sizeof(double));
    printf("Wynik całki w przedziale [%f, %f] z krokiem %f wynosi: %f\n", start, end, step, result);
    close(fd_in);
    close(fd_out);

    return 0;
}