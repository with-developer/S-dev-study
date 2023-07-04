#include <stdio.h>
#include <string.h>

// 계정 생성을 위한 구조체 정의
typedef struct Account
{
    // user, password는 최대 20바이트의 크기를 가질 수 있도록 사이즈 설정
    char user[20] = "";
    char password[20] = "";
}Account;

// Account를 구조체로 갖는 acc배열 20개 생성
Account acc[20];
// 계정 생성 카운트 변수를 선언하고, 1로 초기화
int user_count = 1;



// 계정 생성 함수. 리턴할 값이 따로 없으므로 void로 선언
void create_user() {
    // user_id, user_pw 변수를 선언, 사이즈는 최대 20바이트, 문자열 초기화
    char user_id[20] = "";
    char user_pw[20] = "";
    // 계정 생성이 완료된 경우 이벤트 처리를 위해 success 변수 0으로 초기화
    int success = 0;
    printf("\n===== Create User =====\n");
    // 계정 생성 도중 에러 이벤트 처리를 위해 success가 0이라면 계속 반복
    while (success == 0) {
        printf("Enter Your ID (5~20 characters): ");
        scanf("%s", user_id);
        // 입력된 user_id 문자열 길이 체크
        if (strlen(user_id) < 5 || strlen(user_id) > 20) {
            printf("※ Please enter an ID of 5 to 20 characters.\n※ Restart create user\n\n");
            // 문자열 길이가 부족하거나 많다면, while문을 다시 시작
            continue;
        }

        printf("Enter Your PW (5~20 characters): ");
        scanf("%s", user_pw);
        // 입력된 user_pw 문자열 길이 체크
        if (strlen(user_pw) < 5 || strlen(user_pw) > 20) {
            printf("※ Please enter a PW of 5 to 20 characters.\n※ Restart create user\n\n");
            // 문자열 길이가 부족하거나 많다면, while문을 다시 시작
            continue;
        }

        // 계정 생성에 성공한 경우 이벤트 처리를 위한 변수 i 선언
        int i;
        // 현재 user_count값만큼 for문 반복
        for (i = 1; i < user_count; i++) {
            // acc[i].user에 현재 입력한 값과 동일한 아이디가 존재하는지 체크
            if (strcmp(acc[i].user, user_id) == 0) {
                printf("※ The user is already activated.\n※ Restart create user\n\n");
                // 존재한다면 for문에서 break
                break;
            }
        }
        if (i != user_count) {
            // 이미 존재하는 계정이므로 while문 다시 시작
            continue;
        }
        // strcat 함수를 사용하여 acc[user_count].user에 계정 추가
        strcat(acc[user_count].user, user_id);
        // strcat 함수를 사용하여 acc[user_count].password에 패스워드 추가
        strcat(acc[user_count].password, user_pw);

        printf("※ Created account: %s/%s\n\n", acc[user_count].user, acc[user_count].password);
        // 계정 생성이 완료되었으므로 user_count변수 1 증가
        user_count++;
        // 계정 생성이 완료되었으므로 while문이 돌아가지 않도록 success변수 1 설정
        success = 1;
    }
}

// 가입된 계정을 볼 수 있는 함수
void show_user() {
    printf("\n===== User List =====\n");
    printf("Count Account: %d\n", user_count-1);
    // user_count-1의 값은 현재까지 저장된 계정 변수의 index
    // 따라서, 1부터 user_count-1까지 acc[i].user 출력
    for (int i = 1; i < user_count; i++) {
            printf("%dth Account: %s\n", i, acc[i].user);
        
    }
    printf("\n");
    return;
}

// 로그인 함수
void login() {
    char user_id[20] = "";
    char user_pw[20] = "";
    // user_count이 1이라면 계정 생성이 아직 진행되지 않은 상태
    if (user_count == 1) {
        printf("※ The database is empty!\n\n");
        return;
    }
    printf("\n===== Login =====\n");
    printf("User ID: ");
    scanf("%s", user_id);
    printf("User PW: ");
    scanf("%s", user_pw);

    // 1부터 user_count-1까지 for문
    for (int i = 1; i < user_count; i++) {
        // acc[i].user의 값이 입력한 user_id의 값과 동일하다면
        if (strcmp(acc[i].user, user_id) == 0) {
            // acc[i].password의 값이 입력한 password의 값과 동일하다면
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
