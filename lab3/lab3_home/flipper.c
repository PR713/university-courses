#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/stat.h>

#define MAX_LINE 1024

void process_directory(const char *src_dir, const char *out_dir){
    DIR *dirp = opendir("src_dir");

    if (dirp == NULL) {
        printf("Nie istnieje katalog o podanej ścieżce!");
        return;
    }
    
    struct dirent *an_entry;
    struct stat file_stat;

    char src_path[512], out_path[512];

    while (an_entry = readdir(dirp) != NULL) {
        
        if (an_entry -> d_name[0] == '.'){
            continue;
        }

        snprintf(src_path, sizeof(src_path), "%s/%s", src_dir, an_entry -> d_name);

        if (stat(src_path, &file_stat) == 0 && S_ISREG(file_stat.st_mode)) {
            snprintf(out_path, sizeof(out_path), "%s/%s", out_dir, an_entry -> d_name);
            process_file(src_path, out_path);
        }
    }

    closedir(dirp);
    
}


void process_file(const char* src_path, const char* out_path){
    FILE *src = fopen(src_path, "r");
    if (!src){
        perror("Błąd otwierania pliku źródłowego");
        return;
    }

    FILE *dest = fopen(out_path, "w");
    if (!dest) {
        perror("Błąd tworzenia pliku wynikowego");
        fclose(src);
        return;
    }

    char line[MAX_LINE];
}


int main(int argc, char *argv[]) {

    process_directory(argv[0], argv[1]);

    return 0;
}