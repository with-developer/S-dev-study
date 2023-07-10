#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

struct Student {
    int id;
    char name[20];
    double score;
};

int main()
{
    struct Student* students;
    int student_size=0;
    printf("몇명의 학생을 추가하시겠습니까? >>");
    
    scanf("%d", &student_size);

    students = (struct Student*)malloc(sizeof(struct Student) * student_size);
    
    for (int i = 0; i < student_size; i++) {
        
        int id = 0;
        char name[20];
        double score = 0;

        printf("%d 번째 학생의 id를 입력하세요: ", i + 1);
        scanf("%d", &id);
        students[i].id = id;

        printf("%d 번째 학생의 name을 입력하세요: ", i + 1);
        scanf("%s", name);
        strcpy(students[i].name, name);

        printf("%d 번째 학생의 score를 입력하세요: ", i + 1);
        scanf("%lf", &score);
        students[i].score = score;
    }

    printf("\n입력된 학생 정보:\n");
    for (int i = 0; i < student_size; i++) {
        printf("%d %s %.2f\n", students[i].id, students[i].name, students[i].score);
        
    }

    free(students); // 할당된 동적 메모리 해제
    return 0;
}
