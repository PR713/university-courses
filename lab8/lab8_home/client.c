#include <sys/msg.h>
//#include <sys/ipc.h>

#define MSG_MAX_LEN 256
#define MSG_INIT 1
#define MSG_TEXT 2


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
    int client_queue_id = msgget(client_queue_id, IPC_CREAT | 0666);

    message init_msg = {MSG_INIT, 0, client_key, ""};
    msgsnd(server_queue_id, &init_msg, sizeof(message) - sizeof(long), 0);

    message response;
    msgrcv(client_queue_id, &response, sizeof(message) - sizeof(long), 0, 0);

    int client_id = atoi(response.text);

    

    return 0;
}