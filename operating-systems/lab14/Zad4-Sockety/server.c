#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <signal.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <sys/time.h>
#include <fcntl.h>

#define PORT 12345
#define BUF_SIZE 100
#define MAX_CLIENTS 5

int main()
{
    int server_fd, new_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    char buffer[BUF_SIZE];

    struct sockaddr_in client_addr;
    socklen_t client_len = sizeof(client_addr);
    int server_socket = -1;

    if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
       perror("Error creating socket"); 
       exit(EXIT_FAILURE);
    }   

    /*
    TODO: Utworz socket domeny internetowej typu polaczeniowego
    server_fd = ......
    if (server_fd == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
    */

    int opt = 1;
    setsockopt(server_socket, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    // ustaw odpowiednio parametry struktury adresowej
    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_port = htons(PORT);
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // zbinduj socket do przygotowanej struktury adresowej
    if (bind(server_socket, (struct sockaddr *)&addr, sizeof(struct sockaddr)) < 0) {
        perror("Error binding");
        exit(EXIT_FAILURE);
    }

    // ustaw socket w trybie nasluchu
    listen(server_socket, MAX_CLIENTS);
    printf("Server started on port %d\n", PORT);

    while (1)
    {
        // Doprowadz do akceptacji nadchodzacych polaczen
        new_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_len);
        if (new_socket < 0)
        {
            perror("accept");
            continue;
        }
        
        memset(buffer, 0, BUF_SIZE);
        read(new_socket, buffer, BUF_SIZE);

        char *endptr;
        int num = strtol(buffer, &endptr, 10);
        if (buffer[0] == '\0' || *endptr != '\0')
        {
            write(new_socket, "ERR", 3);
        }
        else
        {
            int result = num + 10;
            char response[BUF_SIZE];
            snprintf(response, BUF_SIZE, "%d", result);
            write(new_socket, response, strlen(response));
        }

        close(new_socket);
    }

    close(server_fd);
    return 0;
}
