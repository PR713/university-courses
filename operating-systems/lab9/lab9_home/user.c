#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include "common.h"

char random_char() {
    return 'a' + rand() % 26;
}


int main() {
    srand(getpid());

    int shmid = shmget(SHM_KEY, sizeof(SharedQueue), 0666);
    SharedQueue* q = (SharedQueue*)shmat(shmid, NULL, 0);

    int semid = semget(QUEUE_SEM_KEY, 3, 0666);

    while (1) {
        PrintTask task;

        for (int i = 0; i < TASK_LEN; i++)
            task.data[i] = random_char();

        sem_op(semid, SEM_EMPTY, -1); //SEM_EMPTY liczba miejsc w kolejce
        sem_op(semid, SEM_MUTEX, -1); //SEM_MUTEX dostęp do kolejki

        q->queue[q->tail] = task;
        q->tail = (q->tail + 1) % QUEUE_SIZE;
        q->count++;

        printf("[USER %d] Sent task: %.10s\n", getpid(), task.data);

        sem_op(semid, SEM_MUTEX, 1);
        sem_op(semid, SEM_FULL, 1); //SEM_FULL czy coś do wydruku jest w kolejce

        sleep(rand() % 5 + 1);

    }

    return 0;
}