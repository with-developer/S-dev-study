#define _CRT_SECURE_NO_WARNINGS
#define column_count 101
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

//구조체 생성
typedef struct logdata {
	char date[20];
	char id[20];
	char pw[20];
	char result[20];
}logdata;

int main()
{
	FILE* pFile = NULL;

	pFile = fopen("log.txt", "r");
	if (pFile == NULL)
	{
		printf("File not open!\n");
		return -1;
	}

	char strTemp[255];
	char* pStr;
	int count = 0;

	logdata log[column_count] = { 0 };

	while (!feof(pFile))
	{
		pStr = fgets(strTemp, sizeof(strTemp), pFile);
		//printf("%s", pStr);

		char* slice_ptr = strtok(pStr, " ");    //첫번째 strtok 사용.
		int index_num = 0;
		while (slice_ptr != NULL)              //ptr이 NULL일때까지 (= strtok 함수가 NULL을 반환할때까지)
		{
			//printf("this data: %s, index_num: %d\n", slice_ptr, index_num);

			if (index_num == 0) {
				strcat(log[count].date, slice_ptr);
			}
			else if(index_num == 1) {
				strcat(log[count].date, " ");
				strcat(log[count].date, slice_ptr);
			}
			else if (index_num == 2) {
				strcat(log[count].id, slice_ptr);
			}
			else if (index_num == 3) {
				strcat(log[count].pw, slice_ptr);
			}
			else if (index_num == 4) {
				strcat(log[count].result, slice_ptr);
			}
			//else {
			//	continue;
			//}
			slice_ptr = strtok(NULL, " ");     //자른 문자 다음부터 구분자 또 찾기
			index_num++;
		}
		count++;
	}

	for (int i = 0; i < column_count-1; i++) {
		printf("%d data\ndate: %s\nusername: %s\npassword: %s\nresult: %s\n\n", i, log[i].date, log[i].id, log[i].pw, log[i].result);
	}
	fclose(pFile);
	
	return 0;

}

