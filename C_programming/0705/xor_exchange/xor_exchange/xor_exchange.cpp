#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>



int main()
{
    int a = 5;
    int b = 6; // 변수의 선언
    



    printf("original value: %d, %d\n", a, b);
    printf("original address: %#x, %#x\n\n", &a, &b);

    a = a ^ b;
    b = a ^ b;
    a = a ^ b;

    printf("changed value: %d, %d\n", a, b);
    printf("changed address: %#x, %#x\n\n", &a, &b);

}

