//wersja z semaforami
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

typedef struct {
    int value;
    sem_t sem1, sem2, sem3;
} SharedData;

void *thread1(void *arg) {
    SharedData *data = (SharedData *)arg;
    
    sem_wait(&data->sem1);  // Czeka na sem1 (dostępny od razu)
    
    // Wykonaj operację
    data->value += 1;
    printf("Thread1: value = %d\n", data->value);
    
    // Pozwól thread2 działać
    sem_post(&data->sem2);
    
    return NULL;
}

void *thread2(void *arg) {
    SharedData *data = (SharedData *)arg;
    
    sem_wait(&data->sem2);  // Czeka na sygnał od thread1
    
    // Wykonaj operację
    data->value += 2;
    printf("Thread2: value = %d\n", data->value);
    
    // Pozwól thread3 działać
    sem_post(&data->sem3);
    
    return NULL;
}

void *thread3(void *arg) {
    SharedData *data = (SharedData *)arg;
    
    sem_wait(&data->sem3);  // Czeka na sygnał od thread2
    
    // Wykonaj operację
    data->value += 3;
    printf("Thread3: value = %d\n", data->value);
    
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <integer>\n", argv[0]);
        return 1;
    }

    char *endptr;
    int input = strtol(argv[1], &endptr, 10);
    if (*argv[1] == '\0' || *endptr != '\0') {
        fprintf(stderr, "Invalid input: not an integer\n");
        return 1;
    }

    SharedData data = {.value = input};

    // Inicjalizacja semaforów
    sem_init(&data.sem1, 0, 1);  // Thread1 może zacząć
    sem_init(&data.sem2, 0, 0);  // Thread2 czeka
    sem_init(&data.sem3, 0, 0);  // Thread3 czeka

    pthread_t t1, t2, t3;

    // Tworzenie wątków
    pthread_create(&t1, NULL, thread1, (void *)&data);
    pthread_create(&t2, NULL, thread2, (void *)&data);
    pthread_create(&t3, NULL, thread3, (void *)&data);

    // Oczekiwanie na zakończenie wątków
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);

    printf("Final value: %d\n", data.value);

    // Czyszczenie semaforów
    sem_destroy(&data.sem1);
    sem_destroy(&data.sem2);
    sem_destroy(&data.sem3);

    return 0;
}