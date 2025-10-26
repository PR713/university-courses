#include <stdio.h>
#include <string.h>

void printMessage(){
    printf("Hello World\n");
}


void greetMe(){
    char name[100];
    scanf("%99s", name);
    printf("Hello %s! \n", name);
}

//static
// gcc -c stringlibrary.c
// ar cr libstringlibrary.a stringlibrary.o
//tworzymy .h i tam deklaracje funkcji
// gcc main.c -o main -L. -lstringlibrary

// shared (współdzielona - linkowana dynamicznie)
// gcc -fPIC -c stringlibrary.c
// gcc -shared -fPIC -o libdynamicstringlibrary.so stringlibrary.o
// gcc dynamicMain.c -o dynamicMain -L. -ldynamicstringlibrary -Wl,-rpath,.

