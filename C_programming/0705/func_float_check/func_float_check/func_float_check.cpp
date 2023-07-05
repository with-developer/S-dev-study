#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


bool float_check(int num) {
    int count = 0;
    for (int i = 1; i <= num; i++) {
        for (int j = 1; j <= num; j++) {
            if (i * j == num) {
                //printf("%d* %d = %d\n",i,j,num);
                count++;
            }
        }
    }
    if (count == 2) {
        return true;
    }
    else {
        return false;
    }

}
int main()
{
    int num = 0;

    printf("값을 입력하세요: ");
    scanf("%d", &num);

    bool result = float_check(num);

    if (result == true) {
        printf("\n%d는 소수입니다.",num);
    }
    else {
        printf("\n%d는 소수가 아닙니다.", num);
    }

   

}

