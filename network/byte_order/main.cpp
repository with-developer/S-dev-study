#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

uint16_t my_ntohs(uint16_t n){
	uint16_t n1 = (n & 0xFF00) >> 8;
	uint16_t n2 = (n & 0x00FF) << 8;
	return n1 | n2;

}

void write_0x1234(){
	uint8_t network_buffer[] = { 0x12, 0x34};
	uint16_t* p =reinterpret_cast<uint16_t*>(network_buffer);
	uint32_t n = my_ntohs(*p);
	printf("32 bit number=0x%x\n", n);
}

int main(){
	write_0x1234();
}
