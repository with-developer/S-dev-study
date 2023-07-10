#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h >

typedef struct lower_upper{
	int is_lowwer = 0;
	int is_upper = 0;
}lower_upper;

struct lower_upper get_lower_upper(char message[100]) {
	struct lower_upper result;

	for (int i = 0; i <= strlen(message); i++) {
		if (isupper(message[i])) {
			result.is_upper++;
		}
		else if (islower(message[i])) {
			result.is_lowwer++;
		}
	}
	return result;
}

int main()
{
	char message[100] = "";

	printf("input text >");
	scanf("%s", &message);

	struct lower_upper operation;
	operation = get_lower_upper(message);
	
	printf("lower count: %d\nupper count: %d", operation.is_lowwer, operation.is_upper);
}