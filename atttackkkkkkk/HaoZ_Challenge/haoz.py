from itertools import product
import string
import math
import hashlib

def blockCipher(input, key):
    print("Decrypting one block")
    #need a way to add byte by byte and concatenate properly
    return input + key


if __name__ == "__main__":

    print("Solving the Hao's challenge")
    iv = hashlib.md5("HAOZ".encode("utf-8")).hexdigest()
    iv = int(iv, 16)
    print("IV ", hex(iv))

    key = hashlib.md5("CTF".encode("utf-8")).hexdigest()
    key = int(key, 16)
    print("KEY", hex(key))

    # 128 bits (16 bytes)
    # iv = 0x09bf1e72affb6a192448a572e11e4620

    # Key is 3 character long, uppercase alphabetical
    # 24bits 3 byte long
    #charList = string.ascii_uppercase
    #keywords = [''.join(i) for i in product(charList, repeat = 3)]

    # First four bytes 0x25 0x50 0x44 0x46 (%PDF)

    inFile = open("secret.pdf", 'rb')
    inputData = inFile.read()
    inFile.close()

    cipherText = int.from_bytes(inputData[0:16], 'little')
    print("CIP", hex(cipherText))

    decrypted = blockCipher(iv, key)
    plainText = decrypted ^ cipherText
    print(hex(plainText))

    if(hex(plainText >> 8*12) == 0x25504446):
        print("Found match!")
        exit()
