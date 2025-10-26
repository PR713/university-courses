#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

typedef struct
{
    int value;
} SharedData;

void *thread_add1(void *arg)
{
    SharedData *data = (SharedData *)arg;
    data->value += 1;
    pthread_exit(NULL);
}

void *thread_add2(void *arg)
{
    SharedData *data = (SharedData *)arg;
    data->value += 2;
    pthread_exit(NULL);
}

void *thread_add3(void *arg)
{
    SharedData *data = (SharedData *)arg;
    data->value += 3;
    pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
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

    pthread_t t1, t2, t3;

    // uruchom funkcje thread_add1, thread_add2 oraz thread_add3 w trzech kolejnych watkach
    // przekazujac data jako liczbe ktora maja zmodyfikowac
    pthread_create(&t1, NULL, (void *) thread_add1, (void *) &data);
    pthread_create(&t2, NULL, (void *) thread_add2, (void *) &data);
    pthread_create(&t3, NULL, (void *) thread_add3, (void *) &data);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    pthread_join(t3, NULL);


    printf("%d\n", data.value);
    fflush(stdout);
    return 0;
}
