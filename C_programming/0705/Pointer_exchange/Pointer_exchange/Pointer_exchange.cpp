#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>



int main()
{
    int a = 100;
    int b = 200; // 변수의 선언
    int temp = 0;
    int* a_ptr = &a; 
    int* b_ptr = &b; // 포인터의 선언
    int* t_ptr = &temp;

    printf("original: %d, %d\n", *a_ptr, *b_ptr);
    printf("original: %#x, %#x\n\n", a_ptr, b_ptr);

    temp = *a_ptr;
    a = *b_ptr;
    b = temp;
    
    printf("change: %d, %d\n", *a_ptr, *b_ptr);
    printf("change: %#x, %#x\n\n", a_ptr, b_ptr);

}

