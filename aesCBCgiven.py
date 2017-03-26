from Crypto.Cipher import AES
from Padding import *

def aesCBCgiven(key, iv, text, mode):
    aes = obj = AES.new(key, AES.MODE_CBC, iv)
    if(mode.lower() == 'e'):
        padded = text
        padded = pad(padded,16,'pkcs7')

        print("padded:             ", padded)
        return aes.encrypt(padded)
    elif(mode.lower() == 'd'):
        decrypted = aes.decrypt(text)
        print("decrypted with pad: ", decrypted)

        unpadded = b''
        try:
            unpadded = unpad(decrypted,16,'pkcs7')

        except ValueError:
            return "Padding error bitch!"

        print("unpadded:           ", unpadded)
        return unpadded
