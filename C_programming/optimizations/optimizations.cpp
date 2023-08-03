#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#include <windows.h>

bool isPrime(int x) {
    if (x <= 1) {
        return false;
    }

    for (int i = 2; i <= sqrt(x); ++i) {
        if (x % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int n = 1000000;
    int* vec;
    int vecSize = 0;
    LARGE_INTEGER st, ed, freq;

    printf("1부터 1,000,000까지 소수 개수를 계산합니다.\n");

    vec = (int*)malloc(n * sizeof(int));

    QueryPerformanceFrequency(&freq);
    QueryPerformanceCounter(&st); // 측정 시작

    for (int i = 0; vecSize < n; ++i) {
        if (isPrime(i)) {
            vec[vecSize++] = i;
        }
    }

    QueryPerformanceCounter(&ed); // 측정 완료

    printf("소요 시간 : %lf\n", (double)(ed.QuadPart - st.QuadPart) / ((double)freq.QuadPart));
    system("pause");

    free(vec);
    return 0;
}
