#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 23 March 2017
# AES-CBC-256

import argparse
from Padding import *
from Crypto.Cipher import AES

def aesCBCself(key, iv, text, mode):
    keyFile = open(key, 'rb')
    keyContent = keyFile.read()
    keyFile.close()

    ivFile = open(iv, 'rb')
    ivContent = ivFile.read()
    ivFile.close()

    textFile = open(text, 'rb')
    textBlock = textFile.read(16)

    output = b''

    if(mode.lower() == 'e'):
        print("encrypting")
        aes = obj = AES.new(keyContent, AES.MODE_CBC, ivContent)
        while textBlock:
            if(len(textBlock)%16 != 0):       #Padding, not sure if want at the end, or check for every block
                textBlock = pad(textBlock,16,'pkcs7')

            ciphertext = aes.encrypt(textBlock)

            XOREd = int.from_bytes(ciphertext, 'little') ^ int.from_bytes(ivContent, 'little') #XOR
            ivContent = XOREd.to_bytes(16, byteorder='little')           #update IV for next stage with ciphertext
            output += XOREd.to_bytes(16, byteorder='little')            # Appending of ciphertext to output
            textBlock = textFile.read(16)    #read 16 bytes

    elif(mode.lower() == 'd'):
        print("decrypting")

    print(output)
    print(len(output))

    textFile.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-iv', dest='ivFile',help='IV file')
    parser.add_argument('-i', dest='inFile',help='data')
    parser.add_argument('-k', dest='keyFile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    inFile=args.inFile
    ivFile=args.ivFile
    keyfile=args.keyFile
    mode = args.mode

    aesCBCself(keyfile, ivFile, inFile,mode)
