#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

// 구조체 생성
typedef struct logdata {
    char date[40];    // Increase size to accommodate space and second slice
    char id[20];
    char pw[20];
    char result[20];
} logdata;

int log_count = 0;

void usage() {
    printf("syntax : log_database.exe <log_file>\n");
    printf("sample : log_database.exe log.txt\n");
}

struct logdata* read_log(const char* filename) {
    char logfile_line[255];

    FILE* pFile = fopen(filename, "r");
    if (pFile == NULL)
    {
        printf("File not open!\n");
        exit(-1);
    }

    while (fgets(logfile_line, sizeof(logfile_line), pFile))
    {
        log_count++;
    }
    rewind(pFile);

    logdata* log = (logdata*)calloc(log_count, sizeof(logdata));
    if (!log)
    {
        printf("Memory allocation failed!\n");
        exit(-1);
    }

    int rowIndex = 0;
    while (fgets(logfile_line, sizeof(logfile_line), pFile))
    {
        char* slice_ptr = strtok(logfile_line, " ");
        int index_num = 0;
        while (slice_ptr != NULL)
        {
            if (index_num == 0) {
                strcat(log[rowIndex].date, slice_ptr);
            }
            else if (index_num == 1) {
                strcat(log[rowIndex].date, " ");
                strcat(log[rowIndex].date, slice_ptr);
            }
            else if (index_num == 2) {
                strcat(log[rowIndex].id, slice_ptr);
            }
            else if (index_num == 3) {
                strcat(log[rowIndex].pw, slice_ptr);
            }
            else if (index_num == 4) {
                size_t len = strlen(slice_ptr);
                if (len > 0 && slice_ptr[len - 1] == '\n') {
                    slice_ptr[len - 1] = '\0';
                }
                strcat(log[rowIndex].result, slice_ptr);
            }
            slice_ptr = strtok(NULL, " ");
            index_num++;
        }
        rowIndex++;
    }

    fclose(pFile);
    printf("로그파일을 성공적으로 읽었습니다!\n");
    return log;
}

void show_database(struct logdata* log) {
    for (int i = 0; i < log_count; i++) {
        printf("%d data\ndate: %s\nusername: %s\npassword: %s\nresult: %s\n\n", i, log[i].date, log[i].id, log[i].pw, log[i].result);
    }
}

void find_user(char username[20], struct logdata* log) {
    int count = 0;
    for (int i = 0; i < log_count; i++) {
        if (strcmp(log[i].id,username) == 0) {
            count++;
            printf("%d data\ndate: %s\nusername: %s\npassword: %s\nresult: %s\n\n", i, log[i].date, log[i].id, log[i].pw, log[i].result);
        }
    }
    printf("find %d column\n", count);
}

void find_result(char result[20], struct logdata* log) {
    printf("%s\n", result);
    int count = 0;
    for (int i = 0; i < log_count; i++) {
        if (strcmp(log[i].result, result) == 0) {
            count++;
            printf("%d data\ndate: %s\nusername: %s\npassword: %s\nresult: %s\n\n", i, log[i].date, log[i].id, log[i].pw, log[i].result);
        }
    }
    printf("find %d column\n", count);
}


int main(int argc, char* argv[]) {
    //if (argc != 2) {
        //usage();
        //return -1;
    //}
    //const char* test = argv[1];
    const char* test = "log.txt";

    struct logdata* log;
    log = read_log(test);


    while (true) {
        int menu = 0;
        int sub_menu = 0;
        printf("\n메뉴를 선택해주세요.\n1. 전체 로그 출력\n2. 로그 검색\n>> ");
        scanf_s("%d", &menu);
        if (menu == 1) {
            printf("전체 로그를 출력하겠습니다.\n");
            show_database(log);
        }
        else if (menu == 2) {
            printf("컬럼을 선택하세요.\n1.계정명\n2.성공/실패 유무\n>> ");
            scanf_s("%d", &sub_menu);
            if (sub_menu == 1) {
                printf("계정명을 입력하세요\n>> ");
                char username[20] = "";
                scanf("%s", username);
                find_user(username, log);
            }
            else if (sub_menu == 2) {
                printf("성공/실패 유무를 입력하세요. (SUCCESS/ERROR)\n>> ");
                char result[20] = "";
                scanf("%s", result);
                find_result(result, log);
            }
            else {
                printf("올바른 값을 입력해주세요.\n");
            }
        }
        else {
            printf("올바른 값을 입력해주세요.\n");
        }
    }


    free(log);
    return 0;
}


