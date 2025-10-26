#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include "common.h"


int main() {
    int shmid = shmget(SHM_KEY, sizeof(SharedQueue), 0666);
    SharedQueue* q = (SharedQueue*)shmat(shmid, NULL, 0);

    int queue_semid = semget(QUEUE_SEM_KEY, 3, 0666);

    int printer_semid = semget(PRINTER_SEM_KEY, PRINTER_COUNT, 0666);

    int printer_id = q->next_printer_id++;

    while (1) {

        sem_op(printer_semid, printer_id, -1);

        sem_op(queue_semid, SEM_FULL, -1);
        sem_op(queue_semid, SEM_MUTEX, -1);

        PrintTask task = q->queue[q->head];
        q->head = (q->head + 1) % QUEUE_SIZE;
        q->count--;

        sem_op(queue_semid, SEM_MUTEX, 1);
        sem_op(queue_semid, SEM_EMPTY, 1);


        printf("[PRINTER %d] Printing: ", getpid());
        fflush(stdout);

        for (int i = 0; i < TASK_LEN; i++) {
            printf("%c", task.data[i]);
            fflush(stdout);
            sleep(1);
        }

        printf("\n");

        sem_op(printer_semid, printer_id, 1);
    }
}