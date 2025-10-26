#include <stdio.h>

int main(){

    // FILE *pF = fopen("test.txt", "a");

    // fprintf(pF, "\nPR713");

    // fclose(pF);


    // if(remove("test.txt") == 0) {
    //     printf("That file was deleted succesfully!");
    // } else 
    // {
    //     printf("That file was NOT deleted");
    // }






    //--- read

    FILE *pF = fopen("C:\\Users\\radsz\\Desktop\\poem.txt", "r");
    char buffer[255];

    if(pF == NULL)
    {
        printf("Unable to open the file!\n");
    }
    else {
        while(fgets(buffer, 255, pF) != NULL) {
          printf("%s", buffer);  
        }
    }

    fclose(pF);

    return 0;
}