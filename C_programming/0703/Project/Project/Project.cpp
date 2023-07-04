#include <stdio.h>
#include <string.h>


typedef struct Account
{
    char user[20] = "";
    char password[20] = "";
}Account;


Account acc[20];
int user_count = 1;


void create_user() {
    char user_id[20] = "";
    char user_pw[20] = "";
    int success = 0;
    printf("\n===== Create User =====\n");
    while (success == 0) {
        printf("Enter Your ID (5~20 characters): ");
        scanf("%s", user_id);
        if (strlen(user_id) < 5 || strlen(user_id) > 20) {
            printf("※ Please enter an ID of 5 to 20 characters.\n※ Restart create user\n\n");
            continue;
        }

        printf("Enter Your PW (5~20 characters): ");
        scanf("%s", user_pw);
        if (strlen(user_pw) < 5 || strlen(user_pw) > 20) {
            printf("※ Please enter a PW of 5 to 20 characters.\n※ Restart create user\n\n");
            continue;
        }

        int i;
        for (i = 1; i < user_count; i++) {
            if (strcmp(acc[i].user, user_id) == 0) {
                printf("※ The user is already activated.\n※ Restart create user\n\n");
                break;
            }
        }
        if (i != user_count) {
            continue; // 이미 존재하는 ID이므로 계정 생성 건너뛰기
        }

        strcat(acc[user_count].user, user_id);
        strcat(acc[user_count].password, user_pw);

        printf("※ Created account: %s/%s\n\n", acc[user_count].user, acc[user_count].password);
        user_count++;
        success = 1;
    }
}


void show_user() {
    printf("\n===== User List =====\n");
    printf("Count Account: %d\n", user_count-1);
    for (int i = 1; i < user_count; i++) {
            printf("%dth Account: %s\n", i, acc[i].user);
        
    }
    printf("\n");
    return;
}

void login() {
    char user_id[20] = "";
    char user_pw[20] = "";
    if (user_count == 1) {
        printf("※ The database is empty!\n\n");
        return;
    }
    printf("\n===== Login =====\n");
    printf("User ID: ");
    scanf("%s", user_id);
    printf("User PW: ");
    scanf("%s", user_pw);


    for (int i = 1; i < user_count; i++) {
        if (strcmp(acc[i].user, user_id) == 0) {
            if (strcmp(acc[i].password, user_pw) == 0) {
                printf("※ Welcome. %s\n\n",user_id);
            }
        }
    }
    return;
}


int main() {

    int menu = 0;

    while(true){
        printf("======= MENU =======\n");
        printf("1. Show User \n2. Create User \n3. Login \n4. Program Exit\n");
        printf("Choice menu: ");
        scanf("%d", &menu);
        if (menu < 1 || menu > 4) {
            printf("※ Please choose 1~4");
            main();
        }
        if (menu == 1) {
            show_user();
        }
        else if(menu == 2) {
            create_user();
        }
        else if (menu == 3) {
            login();
        }
        else if (menu == 4) {
            printf("※ This Program Exit\n\n");
            return 0;
        }
    }


    return 0;
}
