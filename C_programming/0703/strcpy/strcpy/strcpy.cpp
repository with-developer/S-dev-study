#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>


char* custom_strcpy(char* strDestination, const char* strSource) {
    int i = 0;
    while (strSource[i] != '\0') {
        strDestination[i] = strSource[i];
        i++;
    }
    strDestination[i] = '\0';

    return strDestination;
}


int main()
{
    char origin[100];
    char new_string[100];
    printf("input message >>");
    scanf("%99s", origin);

    printf("original value: %s\n", origin);
    custom_strcpy(new_string, origin);
    printf("new_string: %s\n", new_string);
}
