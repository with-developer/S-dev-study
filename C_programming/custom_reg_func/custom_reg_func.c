# define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int reg_func(char* message) {
	for (int i = 0; i <= strlen(message); i++) {
		if (message[i] >= 65 && message[i] <= 90) {
			printf("Find %c\n", message[i]);
			return 1;
		}
	}

	return -1;
}

int main() {
	char message[100];

	printf("input message >>");
	scanf("%99s", message);
	
	int result = reg_func(message);

	if (result == 1) printf("exist upper case\n");
	else printf("not exist upper case\n");

	
}