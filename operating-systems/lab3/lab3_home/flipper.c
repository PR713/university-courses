#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/stat.h>

#define MAX_LINE 1024

void process_directory(const char *src_dir, const char *out_dir){
    DIR *dirp = opendir(src_dir);

    if (!dirp) {
        perror("Błąd otwierania katalogu");
        return;
    }
    
    struct dirent *an_entry;
    struct stat file_stat;

    char src_path[512], out_path[512];

    while ((an_entry = readdir(dirp)) != NULL) {
        
        if (an_entry -> d_name[0] == '.' || !has_txt_extension(an_entry -> d_name)){
            continue;
        }

        snprintf(src_path, sizeof(src_path), "%s/%s", src_dir, an_entry -> d_name);
        
        if (stat(src_path, &file_stat) == 0 && S_ISREG(file_stat.st_mode)) {
            snprintf(out_path, sizeof(out_path), "%s/%s", out_dir, an_entry -> d_name);
            printf("Przetwarzanie pliku: %s -> %s\n", src_path, out_path);
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

    while(fgets(line, MAX_LINE, src)){
        
        reverse_line(line);
        
        fprintf(dest, "%s", line);
    }

    fclose(src);
    fclose(dest);
}


void reverse_line(char *line){
    int len = strlen(line);

    if (len > 0 && line[len - 1] == '\n'){
        len--; //odwracamy ale bez znaku nowej linii, on niech sobie tam zostanie..
    }

    for (int i = 0; i < len / 2; i++){
        char temp = line[i];
        line[i] = line[len - i - 1];
        line[len - i - 1] = temp;
    }
}

int has_txt_extension(const char *filename){
    const char *ext = strrchr(filename, '.');
    return (ext && strcmp(ext, ".txt") == 0);
}


int main(int argc, char *argv[]) {

    if (argc != 3) {
        printf("Zla liczba argumentow!!!\n");
        return -1;
    }

    struct stat st;

    if (stat(argv[2], &st) == -1){
        if (mkdir(argv[2], 0755) == -1){
            perror("Błąd podczas tworzenia katalogu");
            return -1;
        }
    }

    process_directory(argv[1], argv[2]);

    return 0;
}