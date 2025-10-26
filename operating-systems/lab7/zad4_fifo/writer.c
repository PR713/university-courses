#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <errno.h>

// Zadanie:
// Program writer:
// - Przyjmuje dwa argumenty: sciezke do potoku nazwanego (FIFO) i wiadomosc tekstowa.
// - Otwiera FIFO do zapisu (potok moze juz istniec).
// - Wysyla podana wiadomosc do potoku i konczy dziaaanie.

int main(int argc, char **argv) {

    if (argc != 3) {
        return 1;
    }

    mkfifo(argv[1], 0644);
    int fd = open(argv[1], O_WRONLY);

    if (fd == -1) {
        perror("open");
    }

    write(fd, argv[2], strlen(argv[2]));
    close(fd);
    return 0;
}