#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <Windows.h>
#define MAX_LEN 512

int main()
{
    DWORD dwsize = MAX_LEN;
    char strUserName[MAX_LEN] = { 0 };

    int nError = GetUserNameA(strUserName, &dwsize);
    if (!nError) {
        printf("GetUserNameA function is ERROR");
        return -1;
    }

    printf("username: %s\n", strUserName);

    char filename[MAX_LEN] = { 0 };
    sprintf(filename, "C:\\Users\\%s\\source.txt", strUserName);
    printf("filename: %s\n", filename);

    char buff[MAX_LEN];
    DWORD rbytes = 0;
    HANDLE hfile = CreateFile(filename, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (hfile == INVALID_HANDLE_VALUE) {
        printf("Failed to open file\n");
        return -1;
    }

    if (ReadFile(hfile, buff, sizeof(buff) - 1, &rbytes, NULL)) {
        buff[rbytes] = '\0';  // Null-terminate the buffer
        printf("buff: %s\n", buff);
    }
    else {
        printf("Failed to read file\n");
        return -1;
    }

    char filename2[MAX_LEN] = { 0 };
    sprintf(filename2, "C:\\Users\\%s\\Appdata\\Local\\Temp\\destination.txt", strUserName);
    printf("filename2: %s\n", filename2);
    HANDLE hfile2 = CreateFile(filename2, GENERIC_WRITE, FILE_SHARE_WRITE, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);
    WriteFile(hfile2, buff, sizeof(buff) - 1, &rbytes, NULL);


    CloseHandle(hfile);
    CloseHandle(hfile2);
    return 0;
}
