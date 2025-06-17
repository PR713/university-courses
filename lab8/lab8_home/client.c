#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/msg.h>
#include <string.h>

#define MSG_MAX_LEN 256
#define MSG_INIT 1
#define MSG_TEXT 2
#define MSG_SIZE sizeof(message) - sizeof(long)


typedef struct message {
    long mtype;
    int sender_id;
    key_t queue_key;
    char text[MSG_MAX_LEN];
} message;


int main() {

    key_t server_key = ftok(".", 'S');
    int server_queue_id = msgget(server_key, 0);

    key_t client_key = ftok(".", getpid());
    int client_queue_id = msgget(client_key, IPC_CREAT | 0666);

    message init_msg = {MSG_INIT, 0, client_key, ""};
    msgsnd(server_queue_id, &init_msg, MSG_SIZE, 0);

    message response;
    msgrcv(client_queue_id, &response, MSG_SIZE, 0, 0);

    int my_id = atoi(response.text); //id klienta na liście w serwerze

    pid_t pid = fork();

    if (pid == 0) {
        while(1) {
            message msg;
            msgrcv(client_queue_id, &msg, MSG_SIZE, 0, 0);
            printf("Client %d sent a message: %s\n", msg.sender_id, msg.text);
        }
    } else {
        char input[MSG_MAX_LEN];
        while (fgets(input, MSG_MAX_LEN, stdin)) {
            input[strcspn(input, "\n")] = 0;
            message msg = {MSG_TEXT, my_id, 0, ""}; //przekazujemy 0 bo już w server.c mamy zapisane
            //clients[i].queue_id :)
            strncpy(msg.text, input, MSG_MAX_LEN);
            msgsnd(server_queue_id, &msg, MSG_SIZE, 0);
        }
    }

    msgctl(client_queue_id, IPC_RMID, NULL);

    return 0;
}