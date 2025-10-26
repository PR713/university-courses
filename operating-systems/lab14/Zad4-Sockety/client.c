#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 12345
#define BUF_SIZE 100

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <number>\n", argv[0]);
        return 1;
    }

    if (argv[1][0] == '\0')
    {
        fprintf(stderr, "Empty input is not valid.\n");
        return 1;
    }

    char *endptr;
    strtol(argv[1], &endptr, 10);
    if (argv[1][0] == '\0' || *endptr != '\0')
    {
        fprintf(stderr, "Invalid input: not an integer\n");
        return 1;
    }

    int sock = -1;
    sock = socket(AF_INET, SOCK_STREAM, 0);
   
    //TODO: Utworz socket domeny internetowej typu polaczeniowego
    if (sock < 0)
    {
        perror("socket");
        return 1;
    }

    // ustaw odpowiednio parametry struktury adresowej
    struct sockaddr_in addr;

    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    //Polacz sie z serwerem 
    if (connect(sock, (struct sockaddr *)&addr, sizeof(struct sockaddr)) == -1)
    {
        perror("connect");
        return 1;
    }

    //Wyslij przekazana w wywolaniu liczbe do serwera
    char num_str[BUF_SIZE];
    snprintf(num_str, sizeof(num_str), "%s", argv[1]);
    write(sock, num_str, strlen(num_str));

    char buffer[BUF_SIZE] = {0};

    //odczytaj odpowiedz od serwera 
    read(sock, buffer, sizeof(buffer));

    if (strncmp(buffer, "ERR", 3) == 0)
    {
        fprintf(stderr, "Invalid input\n");
        return 1;
    }

    printf("%s\n", buffer);
    fflush(stdout);
    close(sock);
    return 0;
}
