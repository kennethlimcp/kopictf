#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 23 March 2017
# AES demo code for pycrypto package

import os
from aesCBCgiven import aesCBCgiven

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

    encrypted = aesCBCgiven(key,iv,plaintext, 'e')
    print("encypted:           ", encrypted)

    decrypted = aesCBCgiven(key,iv,encrypted, 'd')
    print("decrypted:          ", decrypted)

    if(plaintext == decrypted):
        print ("plaintext == decrypted")
    else:
        print("error")
