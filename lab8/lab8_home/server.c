#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/msg.h>
//#include <sys/ipc.h>

#define MSG_MAX_LEN 256
#define MSG_INIT 1
#define MSG_TEXT 2
#define MAX_CLIENTS 5

typedef struct message {
    long mtype;
    int sender_id;
    key_t queue_key;
    char text[MSG_MAX_LEN];
} message;


typedef struct client_info {
    int id;
    int queue_id;
} client_info;


int main() {

    key_t server_key = ftok(".", 'S');

    if (server_key == -1) {
        perror("ftok");
        return 1;
    }

    int server_queue_id = msgget(server_key, IPC_CREAT | 0666);

    if(server_queue_id == -1) {
        perror("msgget");
        return 1;
    }


    printf("Serwer uruchomiony. Queue ID: %d\n", server_queue_id);

    int client_cnt = 0;
    client_info clients[MAX_CLIENTS];

    while(1) {
        message msg;
        ssize_t received = msgrcv(server_queue_id, &msg, sizeof(message) - sizeof(long), 0, 0);
    
        if (received == -1) {
            perror("msgrcv");
            continue;
        }

        if(msg.mtype == MSG_INIT) {
            if (client_cnt >= MAX_CLIENTS) {
                fprintf(stderr, "Za dużo klientów!\n");
                continue;
            }

            int client_queue_id = msgget(msg.queue_key, 0);

            if (client_queue_id == -1) {
                perror("msgget client");
                continue;
            }

            clients[client_cnt].id = client_cnt + 1;
            clients[client_cnt].queue_id = client_queue_id;

            message reply;
            
            reply.mtype = MSG_TEXT;
            reply.queue_key = 0;
            reply.sender_id = 0;
            snprintf(reply.text, MSG_MAX_LEN, "%d", clients[client_cnt].id);

            msgsnd(client_queue_id, &reply, sizeof(message) - sizeof(long), 0);

            printf("Nowy klient [%d] zarejestrowany.\n", clients[client_cnt].id);

            client_cnt++;

        } else if (msg.mtype == MSG_TEXT) {
            printf("Klient %d wysłał wiadomość: %s\n", msg.sender_id, msg.text);

            for (int i = 0; i < client_cnt; i++){
                if (clients[i].id != msg.sender_id) {
                    msgsnd(clients[i].queue_id, &msg, sizeof(message) - sizeof(long), 0);
                }
            }
        }
    }

    msgctl(server_queue_id, IPC_RMID, NULL);

    return 0;
}