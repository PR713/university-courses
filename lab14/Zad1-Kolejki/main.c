#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <unistd.h>
#include <sys/wait.h>
#include <errno.h>

#define MSG_TYPE 1
#define RESP_TYPE 2

struct msgbuf
{
    long mtype;
    int value;
};

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <number>\n", argv[0]);
        return 1;
    }

    char *endptr;
    long val = strtol(argv[1], &endptr, 10);
    if (*endptr != '\0')
    {
        fprintf(stderr, "Invalid input: not an integer\n");
        return 1;
    }
    int input = (int)val;
    int msqid = 0;


    // Utworz kolejke komunikatow
    key_t key = ftok(".", 0);
    msqid = msgget(key, IPC_CREAT | 0666);

    if (msqid == -1) {
        perror("msgget failed");
        return 1;
    }

    pid_t pid = fork();
    if (pid < 0)
    {
        perror("fork");
        return 1;
    }
    else if (pid == 0)
    {
        struct msgbuf recv_msg;
        
        // odbierz wiadomosci z kolejki
        if (msgrcv(msqid, &recv_msg, sizeof(recv_msg.value), MSG_TYPE, 0) == -1) {
            perror("msgrcv failed");
            exit(1);
        }

        recv_msg.value += 10;
        recv_msg.mtype = RESP_TYPE;

        // odeslij wiadomosc do rodzica
        if (msgsnd(msqid, &recv_msg, sizeof(recv_msg.value), 0) == -1) {
            perror("msgsnd failed");
            exit(1);
        }

        exit(0);
    }
    else
    {
        // Proces macierzysty
        struct msgbuf send_msg;
        send_msg.mtype = MSG_TYPE;
        send_msg.value = input;

        // wyslij wiadomosc przez kolejke
        if (msgsnd(msqid, &send_msg, sizeof(send_msg.value), 0) == -1) {
            perror("msgsnd failed");
            return 1;
        }

        struct msgbuf result_msg;
        // odbierz odpowiedz od procesu potomnego
        if (msgrcv(msqid, &result_msg, sizeof(result_msg.value), RESP_TYPE, 0) == -1) {
            perror("msgrcv failed");
            return 1;
        }

        printf("%d\n", result_msg.value);

        wait(NULL);
        
        //usun kolejke
        if (msgctl(msqid, IPC_RMID, NULL) == -1) {
            perror("msgctl failed");
            return 1;
        }
        
        return 0;
    }
}
