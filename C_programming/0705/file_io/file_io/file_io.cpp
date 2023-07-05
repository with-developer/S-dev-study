#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

char utol(char c) {
    if (97 <= int(c) || int(c)>= 122) {
        printf("소문자 %c",c);
        c = c - 32;
        printf("대문자로 바뀐 %c\n", c);

    }
    else if(65 <= int(c) || int(c) >= 79) {
        printf("대문자%c는",c);
        c = c + 32;
        printf("소문자 %c로 바뀌었습니다 \n", c);
    }
    
    return c;
}

int main()
{
    FILE* fp=NULL;
    FILE* fp2 = NULL;
    char filename[] = "file.txt";
    char filename2[] = "result.txt";
    char c;
    fp = fopen(filename, "r");
    fp2 = fopen(filename2, "w");

    if (fp == NULL) {
        printf("File not open!\n");
        return -1;
    }

    while ((c = fgetc(fp)) != EOF) {
        c = utol(c);
        fprintf(fp2, "%c", c);
    }

    //fprintf(fp2,"%s", "Hello KISIA");
    
}

