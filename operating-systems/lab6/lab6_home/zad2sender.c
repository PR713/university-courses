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
    //here it doesnt matter which program we will launch first, because
    //both programs are doing open on "potok1", then on "potok2"
    //so here we are being blocked on fd_out, but when we launch zad2 here
    // we get "sb" who will read us so we are going to fd_in(...). By reversing
    //launch that works the same way
    //"Domyślnie otwieranie potoku nazwanego w trybie do odczytu blokuje do momentu,
    // gdy jakiś inny proces otworzy potok w trybie do zapisu. Analogicznie w drugą stronę
    // - otwieranie w trybie do zapisu blokuje do momentu, gdy ktoś inny otworzy w trybie do odczytu."

    //There are no writers if all descriptors fd (to write) are closed,
    //in case of stream unnamed fd[1]; until it doesn't happen then read, write, open
    //cause blocking.
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