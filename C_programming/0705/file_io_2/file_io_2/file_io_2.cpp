#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


int main()
{
    FILE* fp = NULL;
    char filename[] = "file.txt";
    char buffer[1024];
    char c;
    fp = fopen(filename, "r+");

    if (fp == NULL) {
        printf("File not open!\n");
        return -1;
    }

    fgets(buffer, sizeof(buffer), fp);
    printf("Before: %s\n", buffer);

    printf("After: %s", buffer);
    for (char c = 65; c <= 70; c++) {
        printf("%c", c);
        fprintf(fp, "%c", c);
    }

    fclose(fp);


}

