#include <stdio.h>
#include <stdint.h>
#include <netinet/in.h>
#include <stdlib.h>

uint32_t read_file(char* filename){
	uint32_t number = 0;

	FILE* file = fopen(filename,"rb");
	if (file == NULL) {
        	printf("Failed to open the file: %s\n", filename);
		exit(1);
    	}

	fread(&number,sizeof(uint32_t), 1, file);
	fclose(file);
	number = ntohl(number);
	
	return number;
}


int main(int argc, char* argv[]) {
    	if (argc != 3) {
        	printf("Usage: %s <file1> <file2>\n", argv[0]);
        	return 1;
    	}
    	
	uint32_t number_a = read_file(argv[1]);
	uint32_t number_b = read_file(argv[2]);
	
	printf("%1$u(0x%1$x) + %2$u(0x%2$x) = %3$u(0x%3$x)\n", number_a, number_b, number_a+number_b);
}
