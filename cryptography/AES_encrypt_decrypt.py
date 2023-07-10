#!/usr/bin/python3

#https://pycryptodome.readthedocs.io/en/latest/src/examples.html#encrypt-data-with-aes

import base64

from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES 
 
def pad(msg, bs):
	#return msg + bytes([AES.block_size - len(msg) % AES.block_size] * (AES.block_size - len(msg) % AES.block_size)) 
	return msg + bytes([bs - len(msg) % bs] * (bs - len(msg) % bs)) 
 
def unpad(msg):
	return msg[:-int(msg[-1])] 
 
 
class AESCipher:

	def __init__(self, bs):
		self.bs = bs
		self.sk = get_random_bytes(bs)
		self.iv = get_random_bytes(16) 

	def encrypt(self, msg):
		pt = pad(msg.encode(), self.bs) 
		cipher = AES.new(self.sk, AES.MODE_CBC, self.iv) 
		return (cipher.encrypt(pt)) 

	def decrypt(self, ct):
		cipher = AES.new(self.sk, AES.MODE_CBC, self.iv) 
		return unpad(cipher.decrypt(ct)).decode() 

	def key(self):
		return (self.sk, self.iv)


aes = AESCipher(32)

msg = "Hello" 
ct = aes.encrypt(msg) 
pt = aes.decrypt(ct) 
(sk, iv) = aes.key()
print('key : ' + str(base64.b64encode(sk)))
print('msg : ' + msg)
print('ct : ' + str(base64.b64encode(ct)))
print('iv : ' + str(base64.b64encode(iv)))
print('pt : ' + pt)


print('========================')
print('========================')


ct = aes.encrypt(msg) 
pt = aes.decrypt(ct) 
(sk, iv) = aes.key()
print('key : ' + str(base64.b64encode(sk)))
print('msg : ' + msg)
print('ct : ' + str(base64.b64encode(ct)))
print('iv : ' + str(base64.b64encode(iv)))
print('pt : ' + pt)


