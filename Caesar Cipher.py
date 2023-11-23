
def ceasarEncryption(key, plainTxt):
    cipherTxt=" "
    for i in plainTxt:
        if i.isalpha():
            char=ord(i)+key
            if char>ord('z'):
                char-=ord('z')
            Eletter=chr(char)
            cipherTxt+=Eletter
        else: 
            print("the plain text contain a non letter character")
            break
    print(cipherTxt)

def ceasarDecryption(key, cipherTxt):
    plainTxt=" "
    for i in cipherTxt:
        if i.isalpha():
            c=ord(i)-key
            if c<ord('a'):
                c+=ord('a')
            elif c>ord('z'):
                c-=ord('z')
            Dletter=chr(c)
            plainTxt+=Dletter
        else: 
            print("the cipher text contain a non letter character")
            break
    print(plainTxt)

ceasarEncryption(3, "manal")
ceasarDecryption(3,"pdqdo" )