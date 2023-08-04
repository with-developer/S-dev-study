#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n = 20;
    printf("Fibonacci of %d = %d\n", n, fibonacci(n));

    return 0;
}
