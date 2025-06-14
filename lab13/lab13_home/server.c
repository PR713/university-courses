//SOCK_DGRAM
//./server 12345
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
#include <pthread.h>

#define MAX_CLIENTS 10
#define MAX_NAME 32
#define BUFFER_SIZE 256
#define ALIVE_INTERVAL 10

typedef struct {
    char name[MAX_NAME];
    struct sockaddr_in client_addr;
    time_t last_alive;
    int active;
} Client;

Client clients[MAX_CLIENTS] = {0};
int server_socket;
pthread_mutex_t clients_mutex = PTHREAD_MUTEX_INITIALIZER;

int find_client_by_addr(struct sockaddr_in *addr) {
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].active && 
            clients[i].client_addr.sin_addr.s_addr == addr->sin_addr.s_addr &&
            clients[i].client_addr.sin_port == addr->sin_port) {
            return i;
        }
    }
    return -1;
}

int find_free_slot() {
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (!clients[i].active) {
            return i;
        }
    }
    return -1;
}

int find_client_by_name(const char *name) {
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].active && strcmp(clients[i].name, name) == 0) {
            return i;
        }
    }
    return -1;
}

void broadcast_message(const char *msg, struct sockaddr_in *exclude_addr) {
    pthread_mutex_lock(&clients_mutex);
    for (int i = 0; i < MAX_CLIENTS; i++) {
        if (clients[i].active && 
            !(clients[i].client_addr.sin_addr.s_addr == exclude_addr->sin_addr.s_addr &&
              clients[i].client_addr.sin_port == exclude_addr->sin_port)) {
            sendto(server_socket, msg, strlen(msg), 0, 
                   (struct sockaddr*)&clients[i].client_addr, sizeof(clients[i].client_addr));
        }
    }
    pthread_mutex_unlock(&clients_mutex);
}

void remove_client(int i) {
    pthread_mutex_lock(&clients_mutex);
    if (i >= 0 && i < MAX_CLIENTS && clients[i].active) {
        printf("Client '%s' disconnected.\n", clients[i].name);
        clients[i].active = 0;
        clients[i].name[0] = '\0';
        memset(&clients[i].client_addr, 0, sizeof(clients[i].client_addr));
        clients[i].last_alive = 0;
    }
    pthread_mutex_unlock(&clients_mutex);
}

void add_client(const char *name, struct sockaddr_in *addr) {
    pthread_mutex_lock(&clients_mutex);
    int slot = find_free_slot();
    if (slot != -1) {
        strncpy(clients[slot].name, name, MAX_NAME - 1);
        clients[slot].name[MAX_NAME - 1] = '\0';
        clients[slot].client_addr = *addr;
        clients[slot].last_alive = time(NULL);
        clients[slot].active = 1;
        printf("Client '%s' connected from %s:%d\n", name, 
               inet_ntoa(addr->sin_addr), ntohs(addr->sin_port));
    }
    pthread_mutex_unlock(&clients_mutex);
}

void handle_message(char *buffer, struct sockaddr_in *client_addr) {
    int client_idx = find_client_by_addr(client_addr);
    
    // Jeśli to nowy klient (pierwszy komunikat to jego nazwa)
    if (client_idx == -1) {
        if (strlen(buffer) > 0 && strlen(buffer) < MAX_NAME) {
            add_client(buffer, client_addr);
            sendto(server_socket, "CONNECTED", 9, 0, 
                   (struct sockaddr*)client_addr, sizeof(*client_addr));
        }
        return;
    }
    
    // update czasu ostatniej aktywności
    pthread_mutex_lock(&clients_mutex);
    clients[client_idx].last_alive = time(NULL);
    pthread_mutex_unlock(&clients_mutex);
    
    if (strncmp(buffer, "LIST", 4) == 0) {
        char list[BUFFER_SIZE] = "Clients:\n";
        pthread_mutex_lock(&clients_mutex);
        for (int j = 0; j < MAX_CLIENTS; j++) {
            if (clients[j].active) {
                strcat(list, clients[j].name);
                strcat(list, "\n");
            }
        }
        pthread_mutex_unlock(&clients_mutex);
        sendto(server_socket, list, strlen(list), 0, 
               (struct sockaddr*)client_addr, sizeof(*client_addr));
               
    } else if (strncmp(buffer, "2ALL", 4) == 0) {
        char msg[BUFFER_SIZE];
        time_t now = time(NULL);
        struct tm *tm_info = localtime(&now);
        char timestamp[20];
        strftime(timestamp, sizeof(timestamp), "%H:%M:%S", tm_info);
        
        snprintf(msg, sizeof(msg), "[%s %s] %s", timestamp, clients[client_idx].name, buffer + 5);
        broadcast_message(msg, client_addr);
        
    } else if (strncmp(buffer, "2ONE", 4) == 0) {
        char target[MAX_NAME];
        sscanf(buffer + 5, "%s", target);
        char *msg_start = strchr(buffer + 5, ' ');
        if (!msg_start) return;
        msg_start++;
        
        int target_idx = find_client_by_name(target);
        if (target_idx != -1) {
            char msg[BUFFER_SIZE];
            time_t now = time(NULL);
            struct tm *tm_info = localtime(&now);
            char timestamp[20];
            strftime(timestamp, sizeof(timestamp), "%H:%M:%S", tm_info);
            
            snprintf(msg, sizeof(msg), "[%s %s -> %s] %s", 
                     timestamp, clients[client_idx].name, target, msg_start);
            sendto(server_socket, msg, strlen(msg), 0, 
                   (struct sockaddr*)&clients[target_idx].client_addr, 
                   sizeof(clients[target_idx].client_addr));
        }
        
    } else if (strncmp(buffer, "STOP", 4) == 0) {
        remove_client(client_idx);
        
    } else if (strncmp(buffer, "ALIVE", 5) == 0) {
        // Odpowiedź na PING - już zaktualizowaliśmy last_alive
    }
}

void* ping_thread(void* arg) {
    while (1) {
        sleep(ALIVE_INTERVAL);
        time_t now = time(NULL);
        
        pthread_mutex_lock(&clients_mutex);
        for (int i = 0; i < MAX_CLIENTS; i++) {
            if (clients[i].active) {
                if (now - clients[i].last_alive > ALIVE_INTERVAL * 2) {
                    printf("Client '%s' timed out.\n", clients[i].name);
                    clients[i].active = 0;
                    clients[i].name[0] = '\0';
                    memset(&clients[i].client_addr, 0, sizeof(clients[i].client_addr));
                    clients[i].last_alive = 0;
                } else if (now - clients[i].last_alive > ALIVE_INTERVAL) {
                    sendto(server_socket, "PING", 4, 0, 
                           (struct sockaddr*)&clients[i].client_addr, 
                           sizeof(clients[i].client_addr));
                }
            }
        }
        pthread_mutex_unlock(&clients_mutex);
    }
    return NULL;
}

void signal_handler(int sig) {
    close(server_socket);
    printf("\nServer shutdown.\n");
    exit(0);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <port>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    signal(SIGINT, signal_handler);

    int port = atoi(argv[1]);
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);

    if ((server_socket = socket(AF_INET, SOCK_DGRAM, 0)) == -1) {
        perror("Error creating socket");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = INADDR_ANY; //wszystkie interfejsy o protokole podanym
    // w lab12_home używałem konkretnego IP

    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("Error binding");
        exit(EXIT_FAILURE);
    }

    printf("UDP Server started on port %d\n", port);

    pthread_t ping_t;
    pthread_create(&ping_t, NULL, ping_thread, NULL);

    char buffer[BUFFER_SIZE];
    while (1) { //nie używamy wielowątkowości/select() bo mamy jeden socket i sprawdzamy
        //po adresach
        memset(buffer, 0, sizeof(buffer));
        ssize_t bytes = recvfrom(server_socket, buffer, sizeof(buffer) - 1, 0,
                                 (struct sockaddr*)&client_addr, &client_len);

        //przychodzi wszystko i jest wysyłane za pomocą server_socket, jedynie odbieramy
        //i przekazujemy żeby nam wyłuskało skąd przyszło i gdzie ma być przesłane (do struct sockaddr)
        if (bytes > 0) {
            buffer[bytes] = '\0';
            handle_message(buffer, &client_addr);
        }
    }

    return 0;
}