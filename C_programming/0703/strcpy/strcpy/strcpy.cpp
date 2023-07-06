#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

void custom_strcpy(char message[100]) {
    char result[100] = "";
    
    for (int i = 0; i < strlen(message); i++) {
        result[i] = message[i];
    }

    printf("result value: %s\n", result);
    printf("result address: %#x\n", &result);

    return;
}

int main()
{
    char message[100] = "";
    scanf("%s", message);

    printf("original value: %s\n", message);
    printf("original address: %#x\n\n", &message);

    custom_strcpy(message);
}

