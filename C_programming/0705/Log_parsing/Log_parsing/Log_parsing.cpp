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

struct logdata read_log(const char* filename) {
    char logfile_line[255];

    FILE* pFile = fopen(filename, "r");
    if (pFile == NULL)
    {
        printf("File not open!\n");
        exit(-1);
    }

    // 라인 수 세기
    while (fgets(logfile_line, sizeof(logfile_line), pFile))
    {
        log_count++;
    }
    rewind(pFile);    // 파일 포인터를 다시 시작으로 이동

    logdata* log = (logdata*)calloc(log_count, sizeof(logdata));    // 동적 메모리 할당
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
                strcat(log[rowIndex].result, slice_ptr);
            }
            slice_ptr = strtok(NULL, " ");
            index_num++;
        }
        rowIndex++;
    }

    for (int i = 0; i < log_count; i++) {
        printf("%d data\ndate: %s\nusername: %s\npassword: %s\nresult: %s\n\n", i, log[i].date, log[i].id, log[i].pw, log[i].result);
    }

    fclose(pFile);
    free(log);    // 동적으로 할당된 메모리 해제
    return *log;
}

void show_database(struct logdata log) {
    for (int i = 0; i < log_count; i++) {
        printf("%d data\ndate: %s\nusername: %s\npassword: %s\nresult: %s\n\n", i, log[i].date, log[i].id, log[i].pw, log[i].result);
    }
}


int main(int argc, char* argv[]){
    //if (argc != 2) {
     //   usage();
      //  return -1;
    //}
    const char* test = "log.txt";

    struct logdata log;
    log = read_log(test);

    show_database(log);

    

    return 0;
}
