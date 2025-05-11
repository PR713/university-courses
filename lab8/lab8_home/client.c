#include <sys/msg.h>
//#include <sys/ipc.h>

#define MSG_MAX_LEN 256

typedef struct message {
    long mtype;
    int sender_id;
    key_t queue_key;
    char text[MSG_MAX_LEN];
} message;


int main() {

    key_t key = 100;
    int id = msgget(key, IPC_CREAT);


    return 0;
}