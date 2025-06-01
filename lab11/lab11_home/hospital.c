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
int medicine_count = MAX_MEDICINE; //initial is MAX, everything is working properly <3
int total_patients = 0;
int patients_remaining = 0;
int pharmacists_remaining = 0;
int pharmacists_total = 0;

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
        int wait_time = rand() % 4 + 2;
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
    if (patients_remaining == 0) {
        pthread_cond_signal(&cond_doctor);
        pthread_cond_broadcast(&cond_pharmacist);
    }
    pthread_mutex_unlock(&mutex);
    return NULL;
}

void* pharmacist_thread(void* arg) {
    int id = *(int*)arg;
    while (1) {
        int wait_time = rand() % 11 + 5;
        print_time();
        printf("Farmaceuta(%d): ide do szpitala, bede za %d s\n", id, wait_time);
        sleep(wait_time);

        pthread_mutex_lock(&mutex);

        if (patients_remaining == 0) {
            pthread_mutex_unlock(&mutex);
            break;
        }

        while (medicine_count >= MAX_MEDICINE && patients_remaining > 0) {
            print_time();
            printf("Farmaceuta(%d): czekam na oproznienie apteczki\n", id);
            pthread_cond_wait(&cond_pharmacist, &mutex);
            if (patients_remaining == 0) {
                pthread_mutex_unlock(&mutex);
                return NULL;
            }
        }

        if (patients_remaining == 0) {
            pthread_mutex_unlock(&mutex);
            break;
        }

        pharmacists_remaining++;

        if (medicine_count < MEDICINE_PER_CONSULTATION) {
            print_time();
            printf("Farmaceuta(%d): budzę lekarza\n", id);
            pthread_cond_signal(&cond_doctor);
        }

        print_time();
        printf("Farmaceuta(%d): dostarczam leki\n", id);
        medicine_count = MAX_MEDICINE;
        sleep(rand() % 3 + 1);
        pharmacists_remaining--;
        print_time();
        printf("Farmaceuta(%d): zakończyłem dostawę\n", id);
        
        pthread_cond_signal(&cond_pharmacist);
        pthread_mutex_unlock(&mutex);
        break;
    }

    return NULL;
}

void* doctor_thread(void* arg) {
    while (1) {
        pthread_mutex_lock(&mutex);

        while (!((awaiting_patients >= MAX_PATIENTS_IN_ROOM && medicine_count >= MEDICINE_PER_CONSULTATION) ||
                (pharmacists_remaining > 0 && medicine_count < MEDICINE_PER_CONSULTATION))) {
            if (patients_remaining == 0) {
                pthread_mutex_unlock(&mutex);
                return NULL;
            }
            pthread_cond_wait(&cond_doctor, &mutex);
        }

        if (patients_remaining == 0) {
            pthread_mutex_unlock(&mutex);
            break;
        }

        print_time();
        printf("Lekarz: budzę się\n");

        if (awaiting_patients >= MAX_PATIENTS_IN_ROOM && medicine_count >= MEDICINE_PER_CONSULTATION) {
            print_time();
            printf("Lekarz: konsultuję pacjentów %d %d %d\n", awaiting_ids[0], awaiting_ids[1], awaiting_ids[2]);
            medicine_count -= MEDICINE_PER_CONSULTATION;
            pthread_mutex_unlock(&mutex);
            sleep(rand() % 3 + 2);
            pthread_mutex_lock(&mutex);
            pthread_cond_broadcast(&cond_patient);
            awaiting_patients = 0;

            if (medicine_count < MEDICINE_PER_CONSULTATION) {
                pthread_cond_broadcast(&cond_pharmacist);
            }
        }
        else if (pharmacists_remaining > 0 && medicine_count < MEDICINE_PER_CONSULTATION) {
            print_time();
            printf("Lekarz: przyjmuję dostawę leków\n");
            medicine_count = MAX_MEDICINE;
            pthread_cond_signal(&cond_pharmacist);
            pthread_mutex_unlock(&mutex);
            sleep(rand() % 3 + 1);
            pthread_mutex_lock(&mutex);
        }

        print_time();
        printf("Lekarz: zasypiam\n");
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Użycie: %s <liczba pacjentów> <liczba farmaceutów>\n", argv[0]);
        return 1;
    }

    total_patients = atoi(argv[1]);
    pharmacists_total = atoi(argv[2]);
    patients_remaining = total_patients;
    srand(time(NULL));

    awaiting_ids = malloc(sizeof(int) * MAX_PATIENTS_IN_ROOM);

    pthread_t doctor;
    pthread_create(&doctor, NULL, doctor_thread, NULL);

    pthread_t* patients_threads = malloc(sizeof(pthread_t) * total_patients);
    pthread_t* pharmacists_threads = malloc(sizeof(pthread_t) * pharmacists_total);

    int* patient_ids = malloc(sizeof(int) * total_patients);
    int* pharmacist_ids = malloc(sizeof(int) * pharmacists_total);

    for (int i = 0; i < total_patients; i++) {
        patient_ids[i] = i + 1;
        pthread_create(&patients_threads[i], NULL, patient_thread, &patient_ids[i]);
    }

    for (int i = 0; i < pharmacists_total; i++) {
        pharmacist_ids[i] = i + 1;
        pthread_create(&pharmacists_threads[i], NULL, pharmacist_thread, &pharmacist_ids[i]);
    }

    for (int i = 0; i < total_patients; i++)
        pthread_join(patients_threads[i], NULL);

    

    pthread_join(doctor, NULL);

    for (int i = 0; i < pharmacists_total; i++)
        pthread_join(pharmacists_threads[i], NULL);

    free(awaiting_ids);
    free(patients_threads);
    free(pharmacists_threads);
    free(patient_ids);
    free(pharmacist_ids);

    return 0;
}