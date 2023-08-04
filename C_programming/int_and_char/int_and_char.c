#include <stdio.h>

int main() {
    int intArr[5] = { 1, 2, 3, 4, 5 };
    char charArr[6] = "hello";

    // 배열의 크기 출력
    printf("Size of intArr: %zu bytes\n", sizeof(intArr));
    printf("Size of charArr: %zu bytes\n", sizeof(charArr));

    // 배열의 내용 출력
    printf("\nContents of intArr:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", intArr[i]);
    }
    printf("\n");

    printf("\nContents of charArr: %s\n", charArr);

    // 각 배열의 첫 번째 원소의 메모리 주소 출력
    printf("\nAddress of intArr[0]: %p\n", &intArr[0]);
    printf("Address of charArr[0]: %p\n", &charArr[0]);

    return 0;
}
