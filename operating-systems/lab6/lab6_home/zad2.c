#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <time.h>
#include <stdlib.h>
#include <fcntl.h>

double function(double x){
    return 4.0/(x*x + 1.0);
}

int main(){

    double start, end, step;

    int fd_in = open("potok1", O_RDONLY);
    int fd_out = open("potok2", O_WRONLY);

    if (fd_in == -1 || fd_out == -1) {
        perror("open");
        exit(1);
    }


    read(fd_in, &start, sizeof(double));
    read(fd_in, &end, sizeof(double));
    read(fd_in, &step, sizeof(double));


    double sum = 0.0;

    for(double x = start; x < end; x += step){
        sum += function(x) * step;
        printf("%f", sum);
    }

    write(fd_out, &sum, sizeof(double));
    close(fd_in);
    close(fd_out);

    return 0;
}