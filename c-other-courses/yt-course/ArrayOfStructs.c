#include <stdio.h>
#include <string.h>

struct Student {
    char name[12];
    float gpa;
};

enum Day{Mon, Tue, Wed, Thu, Fri, Sat, Sun = 123};

int main(){

    struct Student student1 = {"Spongebob", 3.2};
    struct Student student2 = {"Patrick", 2.3};
    struct Student student3 = {"Sandy", 3.9};

    struct Student students[] = {student1, student2, student3};

    for (int i = 0; i < sizeof(students)/ sizeof(students[0]); i++){
        printf("%-10s %.2f \n", students[i].name, students[i].gpa);
    }


    enum Day today = Sun;

    if (today == Sat || today == 123){
        printf("It's weekend!");
    }
    

    return 0;
}