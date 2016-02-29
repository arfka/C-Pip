from Crypto.Cipher import AES
import base64


def encrypt (text): #encrypt text using AES
    s = 16*((len(text)/16)+1)
    msg_text = text.rjust(s)
    secret_key = '1234567890123456'
    cipher = AES.new(secret_key,AES.MODE_ECB)
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    return encoded 
    
    
def decrypt (text): #decrypt text using AES
    secret_key = '1234567890123456'
    cipher = AES.new(secret_key,AES.MODE_ECB)
    decoded = cipher.decrypt(base64.b64decode(text))
    return decoded.strip()  


def encrypt_file (file1, file2): #encrypt file using AES
    f = open (file1, 'rb')
    f1 = open (file2, 'wb')
    text = f.readlines()
    for l in text:
        o = encrypt(l)
        o = o + '\n'
        f1.write(o)
    f1.close()
    f.close() 


def decrypt_file (file1, file2): #decrypt file using AES
    f = open (file1, 'rb')
    f1 = open (file2, 'wb')
    text = f.readlines()
    for l in text:
        o = decrypt(l) + '\n'
        f1.write(o)
    f1.close()
    f.close()

