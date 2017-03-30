#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 23 March 2017
# AES demo code for pycrypto package

import os
from aesCBC import aesCBC

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
  # keyFile = open("key", 'wb')
  # key = generateAesKey()
  # keyFile.write(key)
  keyFile = open("key", 'rb')
  key = keyFile.read()
  keyFile.close()

  # ivFile = open("iv", 'wb')
  # iv = generateIV()
  # ivFile.write(iv)
  ivFile = open("iv", 'rb')
  iv = ivFile.read()
  ivFile.close()

  # plaintextFile = open("plaintext", 'wb')
  # plaintext = generateRandomPlainText()
  # plaintextFile.write(plaintext)
  plaintextFile = open("plaintext", 'rb')
  plaintext = plaintextFile.read()
  plaintextFile.close()

  iv = (0x3dafba429d9eb430b422da802c9fac41).to_bytes(16, 'little')
  key = (0x06a9214036b8a15b512e03d534120006).to_bytes(16, 'little')
  plaintext = str.encode("Single block msg")

  print("Plaintext generated!")
  print("plaintext:          ", plaintext)

  encrypted = aesCBC(key,iv,plaintext, 'e')
  print("encypted:           ", encrypted)

  decrypted = aesCBC(key,iv,encrypted, 'd')
  print("decrypted:          ", decrypted)

  if(plaintext == decrypted):
    print ("plaintext == decrypted")
  else:
    print("error")

  iv = (0x562e17996d093d28ddb3ba695a2e6f58).to_bytes(16, 'little')
  key = (0xc286696d887c9aa0611bbb3e2025a45a).to_bytes(16, 'little')
  plaintext = (0x000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f).to_bytes(32, 'little')

  print("Plaintext generated!")
  print("plaintext:          ", plaintext)

  encrypted = aesCBC(key,iv,plaintext, 'e')
  print("encypted:           ", encrypted)

  decrypted = aesCBC(key,iv,encrypted, 'd')
  print("decrypted:          ", decrypted)

  if(plaintext == decrypted):
    print ("plaintext == decrypted")
  else:
    print("error")
