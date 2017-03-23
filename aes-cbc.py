#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 23 March 2017
# AES-CBC-256

import argparse

def cbc(key, iv, text, mode):
    keyFile = open(key, 'rb')
    keyContent = keyFile.read()
    keyFile.close()

    ivFile = open(iv, 'rb')
    ivContent = ivFile.read()
    ivFile.close()

    textFile = open(text, 'rb')
    textBlock = b'0'

    output = b''

    if(mode.lower() == 'e'):
        print("encrypting")
        while textBlock:
            textBlock = textFile.read(8)    #read 8 bytes
            output += textBlock ^ ivContent #XOR
            ivContent = textBlock           #updated IV for next stage with ciphertext
            print(textBlock)

    elif(mode.lower() == 'd'):
        print("decrypting")

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

    cbc(keyfile, ivFile, inFile,mode)
