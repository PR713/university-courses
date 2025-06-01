#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

#define MAX_PATIENTS_IN_ROOM 3
#define MAX_MEDICINE 6
#define MEDICINE_PER_CONSULTATION 3

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond_doctor = PTHREAD_COND_INITIALIZER;
pthread_cond_t cond_patient = PTHREAD_COND_INITIALIZER;
pthread_cond_t cond_pharmacist = PTHREAD_COND_INITIALIZER;

int awaiting_patients = 0;
int medicine_count = MAX_MEDICINE;
int total_patients = 0;
int patients_remaining = 0;
int pharmacists_awaiting = 0;

int* awaiting_ids;


time_t get_current_time() {
    return time(NULL);
}

void print_time() {
    printf("[%ld] - ", get_current_time());
}


void* patient_thread(void* arg) {
    int id = *(int*)arg;

    while (1) {
        int wait_time = rand() % 3 + 3;
        print_time();
        printf("Pacjent(%d): Ide do szpitala, bede za %d s\n", id, wait_time);
        sleep(wait_time);

        pthread_mutex_lock(&mutex);

        if (awaiting_patients >= MAX_PATIENTS_IN_ROOM) {
            pthread_mutex_unlock(&mutex);
            int retry_in = rand() % 3 + 3;
            print_time();
            printf("Pacjent(%d): za dużo pacjentów, wracam później za %d s\n", id, retry_in);
            sleep(retry_in);
            continue;
        }

        awaiting_ids[awaiting_patients] = id;
        awaiting_patients++;
        print_time();
        printf("Pacjent(%d): czeka %d pacjentów na lekarza\n", id, awaiting_patients);

        if (awaiting_patients == MAX_PATIENTS_IN_ROOM) {
            print_time();
            printf("Pacjent(%d): budzę lekarza\n", id);
            pthread_cond_signal(&cond_doctor);
        }

        pthread_cond_wait(&cond_patient, &mutex);
        pthread_mutex_unlock(&mutex);

        print_time();
        printf("Pacjent(%d): kończę wizytę\n", id);
        break;
    }

    pthread_mutex_lock(&mutex);
    patients_remaining--;
    if (patients_remaining == 0) pthread_cond_signal(&cond_doctor);

    pthread_mutex_unlock(&mutex);
    return NULL;
}

void* pharmacist_thread(void* arg) {
    int id = *(int*)arg;
    while (1) {
        int wait_time = rand() % 11 + 5;
        print_time();
        printf("Farmaceuta(PHARMACIST_ID): ide do szpitala, bede za %d s", wait_time);
        sleep(wait_time);

        pthread_mutex_lock(&mutex);

        if (medicine_count >= MAX_MEDICINE) {
            print_time();
            printf("Farmaceuta(%d): czekam na oproznienie apteczki\n", id);
            pthread_mutex_unlock(&mutex);
            sleep(3);
            continue;
        }

        pharmacists_awaiting++;

        if (medicine_count < MEDICINE_PER_CONSULTATION) {
            print_time();
            printf("Farmaceuta(%d): budzę lekarza\n", id);
            pthread_cond_signal(&cond_doctor);
        }

        pthread_cond_wait(&cond_pharmacist, &mutex);
        print_time();
        printf("Farmaceuta(%d): dostarczam leki\n", id);
        medicine_count = MAX_MEDICINE;
        sleep(rand() % 3 + 1);
        pharmacists_awaiting--;
        print_time();
        printf("Farmaceuta(%d): zakończyłem dostawę\n", id);
        pthread_mutex_unlock(&mutex);
        break;
    }
    return NULL;
}