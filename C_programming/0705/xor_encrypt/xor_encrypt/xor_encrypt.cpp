#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

int main()
{
    FILE* fp = NULL;
    char filename[] = "example.bin";
    uint32_t buffer[10];

    fp = fopen(filename, "rb");

    if (fp == NULL) {
        printf("File not open!\n");
        return -1;
    }

    fread(&buffer, sizeof(buffer), 1, fp);

    for (int i = 0; i < 10; i++) {
        printf("buffer[%d] = %x\n", i, buffer[i]);
    }
}

