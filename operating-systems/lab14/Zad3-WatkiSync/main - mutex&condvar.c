//Poprawna wersja z mutexami i cond variables

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct {
    int value;
    int step;  // Kontroluje kolejność wykonania
    pthread_mutex_t mutex;
    pthread_cond_t cond;
} SharedData;

void *thread1(void *arg) {
    SharedData *data = (SharedData *)arg;
    
    pthread_mutex_lock(&data->mutex);
    
    // Czeka aż będzie można wykonać krok 1
    while (data->step != 1) {
        pthread_cond_wait(&data->cond, &data->mutex);
    }
    
    // Wykonaj operację
    data->value += 1;
    printf("Thread1: value = %d\n", data->value);
    
    // Przejdź do następnego kroku
    data->step = 2;
    pthread_cond_broadcast(&data->cond);
    
    pthread_mutex_unlock(&data->mutex);
    
    return NULL;
}

void *thread2(void *arg) {
    SharedData *data = (SharedData *)arg;
    
    pthread_mutex_lock(&data->mutex);
    
    // Czeka aż będzie można wykonać krok 2
    while (data->step != 2) {
        pthread_cond_wait(&data->cond, &data->mutex);
    }
    
    // Wykonaj operację
    data->value += 2;
    printf("Thread2: value = %d\n", data->value);
    
    // Przejdź do następnego kroku
    data->step = 3;
    pthread_cond_broadcast(&data->cond);
    
    pthread_mutex_unlock(&data->mutex);
    
    return NULL;
}

void *thread3(void *arg) {
    SharedData *data = (SharedData *)arg;
    
    pthread_mutex_lock(&data->mutex);
    
    // Czeka aż będzie można wykonać krok 3
    while (data->step != 3) {
        pthread_cond_wait(&data->cond, &data->mutex);
    }
    
    // Wykonaj operację
    data->value += 3;
    printf("Thread3: value = %d\n", data->value);
    
    // Zakończ
    data->step = 4;
    pthread_cond_broadcast(&data->cond);
    
    pthread_mutex_unlock(&data->mutex);
    
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

    SharedData data = {
        .value = input,
        .step = 1,  // Zaczynamy od kroku 1 (thread1)
        .mutex = PTHREAD_MUTEX_INITIALIZER,
        .cond = PTHREAD_COND_INITIALIZER
    };

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

    // Czyszczenie
    pthread_mutex_destroy(&data.mutex);
    pthread_cond_destroy(&data.cond);

    return 0;
}
