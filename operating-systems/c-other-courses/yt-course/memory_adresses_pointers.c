#include <stdio.h>


void printAge(int *pAge){
    printf("You are %d years old\n", *pAge);
}


int main(){

    // char a = 'X';
    // char b = 'Y';
    // short c[2];

    // printf("%d bytes\n", sizeof(a));
    // printf("%d bytes\n", sizeof(b));
    // printf("%d bytes\n", sizeof(c));

    // printf("%p\n", &a);
    // printf("%p\n", &b);
    // printf("%p\n", &c); 


    int age = 21;
    int *pAge = &age;
    //lub int *pAge = NULL;
    //pAge = &age; //mylące ale przy deklaracji używamy * że to jest wskaźnik 
    //a samo *pAge potem w printf to już dereferencja (pobieranie wartości z adresu będącego
    //value of pAge)


    // printf("Adress of age %p\n", &age);
    // printf("Val of age %d\n", age);

    // printf("Val of pAge   %p\n", pAge); // = &age

    // printf("Adress of pAge %p\n", &pAge); //on jest znów w innym adresie

    // printf("Value at stored address: %d", *pAge);

    //printAge(age);
    printAge(pAge);


    //np array[5] = {...} to array to już wskaźnik na adres pierwszego elementu tablicy
    //array - adres, *array - wartość array[0]
    //czyli np int *p = array można zrobić 

    return 0;

}