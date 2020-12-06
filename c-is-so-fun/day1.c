#include <stdio.h>

int main () {
    FILE *fptr;
    char c;

    fptr = fopen("1.txt", "r");
    if (fptr == NULL) 
    {
        printf("Cannot open file \n");
        return(0);
    }

    // do
    // {
    //     c = fgetc(fptr);
    //     printf ("%c", c);
    // }
    // while (c != EOF);

    char* token = strtok(a_str, delim);

    fclose(fptr);
    return 0; 
}