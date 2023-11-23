from Crypto.Cipher import AES 
from Crypto import Random
import base64

def AESencryption(plainTxt):
    blockSize=16
    padding="*"
    p=lambda s:s+(blockSize-len(s)%blockSize)*padding
    key=Random.new().read(16)
    iv=Random.new().read(16)
    E=AES.new(key,AES.MODE_CBC,iv)
    cipherTxt=E.encrypt(p(plainTxt).encode('utf-8'))
    cipherTxt=base64.b64encode(iv+cipherTxt)
    print(key)
    return cipherTxt

def AESdecryption(key, cipherTxt):
    msgDecode=base64.b64decode(cipherTxt)[16:]
    iv=base64.b64decode(cipherTxt)[:16]
    D=AES.new(key,AES.MODE_CBC,iv)
    plainTxt=D.decrypt(msgDecode)
    plainTxt=plainTxt.decode('utf-8')
    plainTxt=plainTxt.rstrip("*")
    return plainTxt

