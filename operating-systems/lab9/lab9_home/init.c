#include <stdio.h>
#include <sys/shm.h>
#include <sys/sem.h>
#include "common.h"

int main() {
    int shmid = shmget(SHM_KEY, sizeof(SharedQueue), IPC_CREAT | 0666);
    SharedQueue* q = (SharedQueue*)shmat(shmid, NULL, 0);
    q->head = q->tail = q->count = q->next_printer_id = 0;
    shmdt(q);

    int queue_semid = semget(QUEUE_SEM_KEY, 3, IPC_CREAT | 0666);
    semctl(queue_semid, SEM_MUTEX, SETVAL, 1);
    semctl(queue_semid, SEM_EMPTY, SETVAL, QUEUE_SIZE);
    semctl(queue_semid, SEM_FULL, SETVAL, 0);

    int printer_semid = semget(PRINTER_SEM_KEY, PRINTER_COUNT, IPC_CREAT | 0666);
    for (int i = 0; i < PRINTER_COUNT; i++)
        semctl(printer_semid, i, SETVAL, 1);

    printf("System initialized. \n");
    return 0;
}