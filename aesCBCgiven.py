from Crypto.Cipher import AES
from Padding import *

def aesCBCgiven(key, iv, text, mode):
    if(mode.lower() == 'e'):
        aesEncrypt = obj = AES.new(key, AES.MODE_CBC, iv)
        padded = text
        padded = pad(padded,16,'pkcs7')

        # print("padded:             ", padded)
        return aesEncrypt.encrypt(padded)
    elif(mode.lower() == 'd'):
        aesDecrypt = obj = AES.new(key, AES.MODE_CBC, iv)
        decrypted = aesDecrypt.decrypt(text)
        # print("decrypted with pad: ", decrypted)

        unpadded = b''
        try:
            unpadded = unpad(decrypted,16,'pkcs7')

        except ValueError:
            return "Padding error bitch!"

        # print("unpadded:           ", unpadded)
        return unpadded
