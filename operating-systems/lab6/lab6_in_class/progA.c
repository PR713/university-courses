//Prog A przekazuje komunikat do prog B który delikatnie go modyfikuje i przekazuje go z powrotem
//do prog A który drukuje ten komunikat na standardowe wyjście, wyorzystać popen / pclose   

#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

int main() {

    FILE* input = popen("./progB komunikat", "r");
    char buffer[256];
    while(fread( &buffer, 1 , 256, input))
        printf("%s", buffer);

    return 0;
}
