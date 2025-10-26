#include <stdio.h>
#include <string.h>

struct Player
{
    char name[12];
    int score;
};


typedef char user[25];

// struct User{
//     char name[25];
//     char password[12];
//     int id;
// }

typedef struct {
    char name[25];
    char password[12];
    int id;
} User;


int main()
{
    struct Player player1;
    struct Player player2;

    strcpy(player1.name, "Radek");
    player1.score = 4;

    strcpy(player2.name, "Miki");
    player2.score = 5;

    printf("%s %d\n", player1.name, player1.score);
    printf("%s %d\n", player2.name, player2.score);


    //typedef

    //char user1[25] = "Radek";
    user user1 = "Radek";

    // struct User user2 = {"Radek", "Password123", 123};
    // struct User user3 = {"Miki", "password124", 123};

    User user2 = {"Radek", "Password123", 123};
    User user3 = {"Miki", "password124", 123};

    printf("%s %s %d", user2.name, user2.password, user2.id);

    return 0;
}