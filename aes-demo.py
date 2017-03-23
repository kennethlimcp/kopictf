#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 23 March 2017
# AES demo code for pycrypto package

import os
from Crypto.Cipher import AES
from Padding import *

def generateAesKey():
    key = os.urandom(32) # 32 bytes is 32*8 = 256bits
    return key

def generateIV():
    iv = os.urandom(16) # 16 bytes is 16*8 = 128bits
    return iv

def generateRandomPlainText():
    pt = os.urandom(31) # 31 bytes is two blocks
    print("Random text byte size: ", len(pt))
    return pt

def aesFunction(key, iv, text, mode):
    aes = obj = AES.new(key, AES.MODE_CBC, iv)
    if(mode.lower() == 'e'):
        padded = text
        if(len(padded)%16 != 0):
            padded = pad(padded,16,'pkcs7')

            print("padded:             ", padded)
        return aes.encrypt(padded)
    elif(mode.lower() == 'd'):
        decrypted = aes.decrypt(text)
        print("decrypted with pad: ", decrypted)
        unpadded = unpad(decrypted,16,'pkcs7')
        print("unpadded:           ", unpadded)
        return unpadded


if __name__=="__main__":
    keyFile = open("key", 'wb')
    key = generateAesKey()
    keyFile.write(key)
    keyFile.close()

    ivFile = open("iv", 'wb')
    iv = generateIV()
    ivFile.write(iv)
    ivFile.close()

    plaintextFile = open("plaintext", 'wb')
    plaintext = generateRandomPlainText()
    plaintextFile.write(plaintext)
    plaintextFile.close()
    print("Plaintext generated!")
    print("plaintext:          ", plaintext)

    encrypted = aesFunction(key,iv,plaintext, 'e')
    print("encypted:           ", encrypted)

    decrypted = aesFunction(key,iv,encrypted, 'd')
    print("decrypted:          ", decrypted)

    if(plaintext == decrypted):
        print ("plaintext == decrypted")
    else:
        print("error")
