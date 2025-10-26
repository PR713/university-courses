#ifndef COMMON_H
#define COMMON_H

#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>

#define SHM_KEY 12345
#define QUEUE_SEM_KEY 56789
#define PRINTER_SEM_KEY 90123`

#define QUEUE_SIZE 10
#define TASK_LEN 10
#define PRINTER_COUNT 3

typedef struct {
    char data[TASK_LEN];
} PrintTask;

typedef struct {
    int head;
    int tail;
    int count;
    int next_printer_id;
    PrintTask queue[QUEUE_SIZE];
} SharedQueue;

enum { SEM_MUTEX = 0, SEM_EMPTY = 1, SEM_FULL = 2 };

void sem_op(int semid, int sem_num, int op) {
    struct sembuf sb = {sem_num, op, 0}; // 0 - flaga

    semop(semid, &sb, 1); // 1 - liczba operacji, można dać dwie na raz ale kolejność
    //wywołań np SEM_EMPTY -1 na początku w user.c i SEM_EMPTY 1 na końcu pętli
    // ma to kluczowe znaczenie
}

#endif