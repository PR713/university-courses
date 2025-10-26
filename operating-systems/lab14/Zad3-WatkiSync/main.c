//można na dwa sposoby bo tylko zmieniamy 0 lub 1
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define SEM1 PTHREAD_MUTEX_INITIALIZER
#define SEM2 PTHREAD_MUTEX_INITIALIZER
#define SEM3 PTHREAD_MUTEX_INITIALIZER

typedef struct
{
    int value;
    sem_t sem1, sem2, sem3;
} SharedData;


void *thread1(void *arg)
{
    SharedData *data = (SharedData *)arg;

    pthread_mutex_lock(&data->sem1);
    pthread_mutex_lock(&data->sem2);
    pthread_mutex_lock(&data->sem3);
    // Wykonaj na data operacje (data->value += 1) w sposob synchroniczny a nastepnie umozliw dzialanie watkowi t1
    data->value += 1;

    pthread_mutex_unlock(&data->sem1);
    pthread_mutex_unlock(&data->sem2);
    pthread_mutex_unlock(&data->sem3);

    return NULL;
}

void *thread2(void *arg)
{

    pthread_mutex_lock(&data->sem2);
    pthread_mutex_lock(&data->sem3);
    // Wykonaj na data operacje (data->value += 2) w sposob synchroniczny a nastepnie umozliw dzialanie watkowi t2
    data->value += 2;

    pthread_mutex_unlock(&data->sem2);
    pthread_mutex_unlock(&data->sem3);
    return NULL;
}

void *thread3(void *arg)
{
    SharedData *data = (SharedData *)arg;
    pthread_mutex_lock(&data->sem3);
    data->value += 3;
    // Wykonaj na data operacje (data->value += 3) w sposob synchroniczny a nastepnie umozliw dzialanie watkowi t3
    pthread_mutex_unlock(&data->sem3);
    return NULL;
}

int main(int argc, char *argv[])
{       //Nie mogę znaleźć błędu... Radosław Szepielak
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s <integer>\n", argv[0]);
        return 1;
    }

    char *endptr;
    int input = strtol(argv[1], &endptr, 10);
    if (*argv[1] == '\0' || *endptr != '\0')
    {
        fprintf(stderr, "Invalid input: not an integer\n");
        return 1;
    }

    SharedData data = {.value = input};
    // Zainicjalizuj semafory sem1, sem2 oraz sem3 w taki sposob aby watek t1
    // mogl zostac uruchomiony/mogl zadzialac jako pierwszy
    sem_init(&data.sem1, 0, 1);
    sem_init(&data.sem2, 0, 0);
    sem_init(&data.sem3, 0, 0);


    pthread_t t1, t2, t3;
    // uruchom watki t1, t2 oraz t3 z funkcjami odpowiednio thread1, thread2 oraz thread3

    pthread_create(&t1, NULL, (void *) thread1, (void *) &data);
    pthread_create(&t2, NULL, (void *) thread2, (void *) &data);
    pthread_create(&t3, NULL, (void *) thread3, (void *) &data);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);


    printf("%d\n", data.value);
    fflush(stdout);

    sem_destroy(&data.sem1);
    sem_destroy(&data.sem2);
    sem_destroy(&data.sem3);

    return 0;
}
