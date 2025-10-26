#include <stdio.h>
#include <ctype.h>

void szyfr_Cezara(char *text, int k) {
    while (*text) { // *text przechowuje kolejne znaki, a text to wskaźnik
        if (isalpha(*text)) { // jeżeli jest literą a nie cyfrą
            
            int is_upper = isupper(*text);// Określenie wielkości litery

            int char_index = is_upper ? *text - 'A' : *text - 'a';// Znalezienie indeksu litery w ASCII

            int new_index = (char_index + k) % 26;// Zastosowanie przesunięcia

            char new_char = is_upper ? new_index + 'A' : new_index + 'a';// Znalezienie nowej litery

            *text = new_char;// Zamiana oryginalnej litery na zaszyfrowaną
        }
        text++;// Przesunięcie wskaźnika na następny znak
    }
}

int main() {
    char plaintext[] = "Reniu Kocham Cie!";
    int shift = 3;

    printf("Oryginal: %s\n", plaintext);

    // Szyfrowanie tekstu
    szyfr_Cezara(plaintext, shift);

    printf("Szyfr: %s\n", plaintext);

    return 0;
}