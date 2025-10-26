#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void birthday(char name[], int age){
    printf("\nHappy birthday dear %s", name);
    printf("\nYou are %d years old!", age);
}

int findMax(int x, int y) {
    return x > y ? x : y;
}

void hello(char[], int); //function prototype


void sort(int array[], int size){
    bool swapped;

    for(int i = 0; i < size - 1; i++) {
        swapped = false;
        for(int j = 0; j < size - i - 1; j++){
            if(array[j] > array[j + 1]) {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                swapped = true;
            }
        }
        
        if (!swapped) {
            break;
        }
        
    }
}


void printArray(int array[], int size){
    for( int i = 0; i < size; i++){
        printf("%d ", array[i]);
    }
}


int main() {

    // printf("Hello!\n");
    // printf("It's really amazing.\n");
    
    // printf("\"Szóstka Wron\" - Leigh Bardugo\n");

    // char name[] = "PoweR";
    // int id = 713;

    // printf("Github profile name %s%d \n", name, id);
    // //f float, c char


    // bool e = true;

    // char f = 101; // range -128 to +127, %d or %c to convert to ASCII

    // int x = 5;
    // int y = 2;
    // float z = (float) x / y;
    // printf("%f", z);




    // char name[25];
    // int age;

    // printf("What's your name?\n");
    // //scanf("%s", &name);
    // fgets(name, 25, stdin); //jeśli np "Radek PR" i są spacje należy użyć
    // name[strlen(name)-1] = '\0';

    // printf("How old are you?\n");
    // scanf("%d", &age);

    // printf("%s, you are %d years old", name, age);



    // double A = sqrt(9);
    // double B = pow(2,4);
    

    // printf("\n%lf", A);



    // const double PI = 3.14159;
    // double radius;
    // double circumference;

    // printf("\nEnter radius of a circle: ");
    // scanf("%1lf", &radius);

    // circumference = 2 * PI * radius;

    // printf("circumference: %lf", circumference);




    // double A;
    // double B;
    // double C;

    // printf("Enter side A: ");
    // scanf("%lf", &A);

    // printf("Enter side B: ");
    // scanf("%lf", &B);

    // C = sqrt(A*A + B*B);

    // printf("Side C: %lf", C);


    // char grade;
    // printf("\n Enter a letter grade: ");
    // scanf("%c", &grade);

    // switch(grade){
    //     case 'A':
    //         printf("perfect!\n");
    //         break;
    //     case 'B': 
    //         printf("You did good!\n");
    //         break; //...
    //     default:
    //         printf("Ups");
    // }



    // char unit;
    // float temp;

    // printf("\nIs the temperature in (F) or (C)?: ");
    // scanf("%c", &unit);
    // unit = toupper(unit);
    
    // if(unit == 'C') {
    //     printf("Enter the temp in C: ");
    //     scanf("%f", &temp);
    //     temp = (temp * 9 / 5) + 32;
    // }
    // else if(unit == 'F'){
    //     printf("Enter the temp in F: ");
    //     scanf("%f", &temp);
    //     printf("\nThe temp in F is: %.1f", temp);
    //     temp = (temp - 32) * 5 / 9;
    // }
    // else {
    //     printf("\n %c is not a valid unit", unit);
    // }




    // char operator;
    // double num1;
    // double num2;
    // double result;

    // printf("\nEnter an operator (+ - * /): ");
    // scanf("%c", &operator);

    // printf("Enter number 1: ");
    // scanf("%lf", &num1);
    // printf("Enter number 2: ");
    // scanf("%lf", &num2);

    // switch(operator){
    //     case '+':
    //         result = num1 + num2;
    //         printf("\nresult: %.2lf", result);
    //         break;
    //     case '-':
    //         result = num1 - num2;
    //         printf("\nresult: %.2lf", result);
    //         break;
    //     case '*':
    //         result = num1 * num2;
    //         printf("\nresult: %.2lf", result);
    //         break;
    //     case '/':
    //         if (num2 == 0) {
    //             printf("%lf can not be 0!!!", num2);
    //             break;
    //         }
    //         result = num1 / num2;
    //         printf("\nresult: %.2lf", result);
    //         break;

    //     default:
    //         printf("%c is not valid", operator);
    // }



    // char name[] = "Radek";
    // int age = 21;

    // birthday(name, age);

    // printf("\n%d", findMax(3, 4));
    // hello(name, age);



    // int i = 5;
    // int a = ++i; 
    // int b = i++;
    // printf("%d%d%d",a , b, i);


    // char name[25];

    // printf("\nWhat's your name?: ");
    // fgets(name, 25, stdin);
    // name[strlen(name) - 1] = '\0';

    // while(strlen(name) == 0)
    // {
    //     printf("\nWhat's your name?: ");
    //     fgets(name, 25, stdin);
    //     name[strlen(name) - 1] = '\0';
    //     printf("You did not enter your name");
    // }

    // printf("Hello %s", name);


    // int number = 0;
    // int sum = 0;

    // do {
    //     printf("Enter num above 0: ");
    //     scanf("%d", &number);
    //     if (number > 0)
    //     {
    //         sum += number;
    //     }

    // } while(number > 0);

    // printf("%d", sum);




    // double prices[] = {5.0, 10.0, 15.0};

    // printf("%lf\n", prices[1]);
    // printf("%d bytes\n", sizeof(prices));

    // char name[] = "Radek";



    // int numbers[2][3] = {{1, 2, 3},
    //                      {4, 5, 6}};


    // char cars[][10] = {"Mustang", "Corvette", "Camaro"};

    // //cars[0] = "Tesla"; Error

    // strcpy(cars[0], "Tesla");

    // for(int i = 0; i < sizeof(cars)/sizeof(cars[0]); i++){
    //     printf("%s\n", cars[i]);
    // }


    // char x[15] = "lemonade";
    // char y[15] = "soda";
    // char temp[15];

    // strcpy(temp, x);
    // strcpy(x, y);
    // strcpy(y, temp);




    int array[] = {9, 1, 3, 4, 5, 8, 2, 1, 9};
    int size = sizeof(array)/sizeof(array[0]);

    sort(array, size);
    printArray(array, size);

    return 0;
}


void hello(char name[], int age){
    printf("\n%s %d", name, age);
}
