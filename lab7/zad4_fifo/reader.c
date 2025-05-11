#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <errno.h>
#include <string.h>

// Zadanie:
// Program reader:
// - Przyjmuje dwa argumenty:sciezke do potoku nazwanego (FIFO) i rozmiar bufora.
// - Otwiera (lub tworzy) potok nazwany do odczytu.
// - Czyta dane z FIFO blokami o zadanym rozmiarze i wypisuje kazdy z nich jako osobny komunikat.
// - Konczy dzialanie, gdy nadawca zakonczy pisanie.

int main(int argc, char* argv[]) {

    if (argc != 3) {
        return 1;
    }
    size_t size = atoi(argv[2]);

    int fd = open(argv[1], O_RDONLY);

    if (fd == -1) {
        mkfifo(argv[1], 0644);
    }
    fd = open(argv[1], O_RDONLY);

    char buffer[size];

    while (read(fd, buffer, size) > 0) {
        printf("%s\n", buffer);
    }

    close(fd);
    return 0;
}