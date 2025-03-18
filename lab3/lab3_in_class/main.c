#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <time.h>


void read_the_file(int fd) {
    char c;
    while(read(fd, &c, 1) == 1)
        printf("%c", c);
    
    printf("\n");
}

void read_the_char_at(int fd, int offset) {

    lseek(fd, offset, SEEK_SET);

    char c;
    read(fd, &c, 1);


    printf("Pozycja %d: %c \n", offset, c);
    
}

void read_the_file_by_512chunks(int fd) {
    char blok[512];
    int cnt = 0;

    while(read(fd, blok, sizeof(blok)) > 0){
        printf("%s", blok);
        cnt += 1;
        printf("\n\n chunk '%d' ---------------------------------------------\n\n", cnt);
    }
        
}

void read_starting_with_position(int fd, int offset) {
    lseek(fd, offset, SEEK_SET);

    char c;
    read(fd, &c, 1);
    printf("%c", c);

}

int main() {
    

    // int fd;
    // fd = open("./plik.txt", O_RDONLY);
    // read_the_file(fd);
    

    // fd = open("./plik.txt", O_RDONLY);
    // read_the_char_at(fd, 3);
    // close(fd);
    
    printf("\n\n---------------------------------------------\n\n");


    clock_t start_char = clock();

    int fd1 = open("./plikV1.txt", O_RDONLY);
    read_the_file(fd1);

    clock_t end_char = clock();

    float time = (float) (end_char - start_char)/CLOCKS_PER_SEC;



    printf("\n\n---------------------------------------------\n\n");


    clock_t start_chunk = clock();

    fd1 = open("./plikV1.txt", O_RDONLY);
    read_the_file_by_512chunks(fd1);

    clock_t end_chunk = clock();

    float time1 = (float) (end_chunk - start_chunk)/CLOCKS_PER_SEC;



    printf("\n\n---------------------------------------------\n\n");


    clock_t start_char_with_position = clock();

    // tutaj ma być znak po znaku a nie na raz !!! i za każdym razem open i close
    fd1 = open("./plikV1.txt", O_RDONLY);
    read_starting_with_position(fd1, 100);

    clock_t end_char_position = clock();

    float time2 = (float) (end_char_position - start_char_with_position)/CLOCKS_PER_SEC;
    
    close(fd1);

    printf("by char: %f\nby chunks: %f\nby char position: %f", time, time1, time2);

    return 0;
}
