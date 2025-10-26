
#include <stdio.h>
#include <stdlib.h>

#define NUMBER_OF_CARDS 52
#define NUMBER_OF_COLORS 4

int out_of_a = 0, out_of_b = 0, lenA = NUMBER_OF_CARDS / 2, lenB = NUMBER_OF_CARDS / 2;


int random_from_interval(int a, int b) {
    return rand() % (b - a + 1) + a;
}

void shuffle(int t[], int size) {
    int k, tmp;
    for (int i = 0; i < size; i++) t[i] = i;
    for (int i = 0; i < size - 1; i++) {
        k = random_from_interval(i, size - 1);
        tmp = t[i];
        t[i] = t[k];
        t[k] = tmp;
    }
}

void cbuff_push(int tab[], int cli_nr, char player) {
    if (player == 'a') tab[(out_of_a + lenA++) % NUMBER_OF_CARDS] = cli_nr;
    else tab[(out_of_b + lenB++) % NUMBER_OF_CARDS] = cli_nr;
}

int cbuff_pop(int t[], char player) {
    if (player == 'a') {
        if (lenA == 0) return -1;
        lenA--;
        int tmp = out_of_a;
        out_of_a = (out_of_a + 1) % NUMBER_OF_CARDS;
        return t[tmp];
    }
    else {
        if (lenB == 0) return -1;
        lenB--;
        int tmp = out_of_b;
        out_of_b = (out_of_b + 1) % NUMBER_OF_CARDS;
        return t[tmp];
    }
}

void print_deck(int t[], char player) {
    if (player == 'b') {
        for (int i = 0; i < lenB; i++) printf("%d ", t[(out_of_b + i) % NUMBER_OF_CARDS]);
    }
    else {
        for (int i = 0; i < lenB; i++) printf("%d ", t[(out_of_a + i) % NUMBER_OF_CARDS]);
    }
}

void game(int n, int player_A[], int player_B[], int max_conflicts, int simplified_mode) {
    int curr_conflicts = 0;
    switch (simplified_mode) {
    case 0:
        while (curr_conflicts <= max_conflicts) {
            if (lenA == 0) {
                printf("3\n");
                print_deck(player_B, 'b');
                break;
            }
            else if (lenB == 0) {
                printf("2 %d", curr_conflicts);
                break;
            }
            if ((int)player_A[out_of_a] / 4 > (int)player_B[out_of_b] / 4) {
                int a = cbuff_pop(player_A, 'a');
                int b = cbuff_pop(player_B, 'b');
                cbuff_push(player_A, a, 'a');
                cbuff_push(player_A, b, 'a');
            }
            else if ((int)player_A[out_of_a] / 4 < (int)player_B[out_of_b] / 4) {
                int a = cbuff_pop(player_A, 'a');
                int b = cbuff_pop(player_B, 'b');
                cbuff_push(player_B, b, 'b');
                cbuff_push(player_B, a, 'b');
            }
            else {
                int cards = 3;
                curr_conflicts++;
                while (lenA >= cards && lenB >= cards && (int)player_A[(out_of_a + cards - 1) % NUMBER_OF_CARDS] / 4 == (int)player_B[(out_of_b + cards - 1) % NUMBER_OF_CARDS] / 4) {
                    cards += 2;
                    curr_conflicts++;
                    if (curr_conflicts > max_conflicts) {
                        printf("0 %d %d", lenA, lenB);
                        break;
                    }
                }
                if (lenA < cards || lenB < cards) {
                    printf("1 %d %d", lenA, lenB);
                    break;
                }
                else if ((int)player_A[(out_of_a + cards - 1) % NUMBER_OF_CARDS] / 4 > (int)player_B[(out_of_b + cards - 1) % NUMBER_OF_CARDS] / 4) {
                    for (int i = 0; i < cards; i++) {
                        int a = cbuff_pop(player_A, 'a');
                        cbuff_push(player_A, a, 'a');
                    }
                    for (int i = 0; i < cards; i++) {
                        int b = cbuff_pop(player_B, 'b');
                        cbuff_push(player_A, b, 'a');
                    }
                }
                else {
                    for (int i = 0; i < cards; i++) {
                        int b = cbuff_pop(player_B, 'b');
                        cbuff_push(player_B, b, 'b');
                    }
                    for (int i = 0; i < cards; i++) {
                        int a = cbuff_pop(player_A, 'a');
                        cbuff_push(player_B, a, 'b');
                    }
                }
            }
            curr_conflicts++;
        }
        if (curr_conflicts > max_conflicts) {
            printf("0 %d %d", lenA, lenB);
            break;
        }
        break;
    case 1:
        while (curr_conflicts <= max_conflicts) {
            if (lenA == 0) {
                printf("3\n");
                print_deck(player_B, 'b');
                break;
            }
            else if (lenB == 0) {
                printf("2 %d", curr_conflicts);
                break;
            }
            if ((int)player_A[out_of_a] / 4 > (int)player_B[out_of_b] / 4) {
                int a = cbuff_pop(player_A, 'a');
                int b = cbuff_pop(player_B, 'b');
                cbuff_push(player_A, a, 'a');
                cbuff_push(player_A, b, 'a');
            }
            else if ((int)player_A[out_of_a] / 4 < (int)player_B[out_of_b] / 4) {
                int a = cbuff_pop(player_A, 'a');
                int b = cbuff_pop(player_B, 'b');
                cbuff_push(player_B, b, 'b');
                cbuff_push(player_B, a, 'b');
            }
            else {
                int a = cbuff_pop(player_A, 'a');
                int b = cbuff_pop(player_B, 'b');
                cbuff_push(player_A, a, 'a');
                cbuff_push(player_B, b, 'b');
            }
            curr_conflicts++;
        }
        if (curr_conflicts > max_conflicts) {
            printf("0 %d %d", lenA, lenB);
            break;
        }
        break;
    default:
        break;
    }
}

int main(void) {
    int player_A[NUMBER_OF_CARDS], player_B[NUMBER_OF_CARDS];
    int deck[NUMBER_OF_CARDS];
    int max_conflicts;
    int simplified_mode;
    int seed;
    scanf("%d", &seed);
    scanf("%d", &simplified_mode);
    scanf("%d", &max_conflicts);

    for (int i = 0; i < NUMBER_OF_CARDS; i++) deck[i] = i;
    srand((unsigned)seed);
    shuffle(deck, NUMBER_OF_CARDS);
    for (int i = 0; i < NUMBER_OF_CARDS / 2; i++) {
        player_A[i] = deck[i];
        player_B[i] = deck[i + NUMBER_OF_CARDS / 2];
    }
    game(NUMBER_OF_CARDS, player_A, player_B, max_conflicts, simplified_mode);
    return 0;
}