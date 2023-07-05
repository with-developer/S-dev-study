#include <stdio.h>

void printEvenNumbers(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) {
            printf("%d ", arr[i]);
        }
    }
    printf("\n");
}

int main() {
    int numbers[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int size = sizeof(numbers) / sizeof(numbers[0]);

    printEvenNumbers(numbers, size);

    return 0;
}
