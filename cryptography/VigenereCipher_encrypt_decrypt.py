# 65 ~ 90 사이가 대문자
# 97 ~ 122 소문자

def encrypt(key, plaintext):
    plaintext_list = [ord(text)-97 for text in plaintext if text.isalpha()]
    key_list = [ord(text)-97 for text in key if text.isalpha()]
    result = []
    
    key_len = len(key)
    
    for idx, ord_num in enumerate(plaintext_list):
        i=idx%key_len
        result_ord_num = ord_num+key_list[i] 
        # 값이 26이 넘는다면 26을 빼줌
        if result_ord_num >= 26:
            result_ord_num -= 26
        
        # 값이 알파벳 범위 이외의 값이라면 공백처리시킴
        if 0 <= result_ord_num <= 25:
            result_ord_num += 97
        else:
            result_ord_num = 32
        result.append(chr(result_ord_num))
        
    # result 리스트를 문자열로 합침
    result = ''.join(result)
    return result


def decrypt(key, encrpttext):
    encrpttext_list = [ord(text)-97 for text in encrpttext if text.isalpha()]
    key_list = [ord(text)-97 for text in key if text.isalpha()]
    result = []
    
    key_len = len(key)
    
    for idx, ord_num in enumerate(encrpttext_list):
        i=idx%key_len
        result_ord_num = ord_num-key_list[i] 
        # 값이 0보다 작다면 26 더해줌
        if result_ord_num < 0:
            result_ord_num += 26
        
        # 값이 알파벳 범위 이외의 값이라면 공백처리시킴
        if 0 <= result_ord_num <= 25:
            result_ord_num += 97
        else:
            result_ord_num = 32
        result.append(chr(result_ord_num))
        
    # result 리스트를 문자열로 합침
    result = ''.join(result)
    return result


# 암/복호화 선택
operation = input("암호화(e) 또는 복호화(d)를 선택하세요: ")
key = input("키를 입력하세요: ")

if operation.lower() == 'e':
    plaintext = input("평문을 입력하세요: ")
    result = encrypt(key.lower(), plaintext.lower())
    print("암호화 결과:",result)
elif operation.lower() == 'd':
    encrypted_text = input("암호문을 입력하세요: ")
    result = decrypt(key.lower(), encrypted_text.lower())
    print(result)
else:
    print("잘못된 작업을 선택하셨습니다.")