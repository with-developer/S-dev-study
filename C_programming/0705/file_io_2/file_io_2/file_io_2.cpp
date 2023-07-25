#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

typedef struct Example1 {
    int a;
    char b;
    short c;
    long d;
    char* e;
    short f;
    int* g;
}Example1;

int main()
{
    Example1 ex1;
    printf("a size = %d\n", sizeof(ex1.a));
    printf("b size = %d\n", sizeof(ex1.b));
    printf("c size = %d\n", sizeof(ex1.c));
    printf("d size = %d\n", sizeof(ex1.d));
    printf("e size = %d\n", sizeof(ex1.e));
    printf("f size = %d\n", sizeof(ex1.f));
    printf("g size = %d\n", sizeof(ex1.g));  

    printf("Total struct size = %d\n", sizeof(Example1));


}

