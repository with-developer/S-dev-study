from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(msg, bs):
    return msg + bytes([bs - len(msg) % bs] * (bs - len(msg) % bs))

def unpad(msg):
    return msg[:int(msg[-1])]



class AESCipher:
    def __init__(self, bytes):
        self.sk = get_random_bytes(bytes)
        self.bs = bytes
        self.iv = get_random_bytes(16)
        
    def encrypt(self, msg):
        pt = pad(msg.encode(), self.bs)
        cipher = AES.new(self.sk, AES.MODE_CBC, self.iv)
        return cipher.encrypt(pt)
    
    def decrypt(self, ct):
        cipher = AES.new(self.sk, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(ct)).decode()
    
    def key(self):
        #return (self.sk, self.iv)
        return self.sk
    
msg = "Hello"
aes = AESCipher(32)
ct = aes.encrypt(msg)
pt = aes.decrypt(ct)
#(sk,iv) = aes.key()

print("Key:", str(base64.b64encode(aes.key())))
print("msg:", msg)
print("ct:", str(base64.b64encode(ct)))
#print("iv:", str(base64.b64encode(iv)))
print("pt:", pt)