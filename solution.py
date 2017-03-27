#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 26 March 2017
# Full solution proof of concept
# Pair programmed with Ryan Lim

from aesCBCgiven import aesCBCgiven
from Padding import *
import os

if __name__=="__main__":
    print("Starting attack :)")

    iv =  str.encode("1234567890123456")
    key =  str.encode("1234567890123456")
    # 2 blocks of repeating "1234567890123456" string + "123456789012345"
    # plainText =  str.encode("12345678901234561234567890123456123456789012345")
    # plainText =  str.encode("1234567890123456ABCDEFGHIJKLMNOP1234567890123456abcdefghjklmnop")
    # plainText =  str.encode("12345678901234561234567890123456123456789012345")

    plainText = os.urandom(62)
    encrypted = aesCBCgiven(key,iv,plainText, 'e')
    decrypted = aesCBCgiven(key,iv,encrypted, 'd')



    print("plaintext:          ", plainText)
    print("encypted:           ", encrypted)
    print("decrypted:          ", decrypted)

    if(plainText == decrypted):
      print ("plaintext == decrypted")
    else:
      print("error")

    print("\n\nPerforming mutation")

    for plainTextLength in range(16*3, 16*5):
        print("plainTextLength", plainTextLength)

        plainText = os.urandom(plainTextLength)
        encrypted = aesCBCgiven(key,iv,plainText, 'e')

        correctByteArray = []
        bytesInCipherText = len(encrypted)
        blocksOfCipherText = int(bytesInCipherText / 16)

        pos = bytesInCipherText - 1


        for round in range(blocksOfCipherText-1):
            # print("pos", pos)
            possibleValues = []

            for pad in range(1,17):
                mutatedBytes = b''
                # print("pad", pad)
                if(pad > 1):
                    for counter in range(0, pad-1):
                        mutatedBytes = (encrypted[((blocksOfCipherText-1)*16)-1-counter] ^ correctByteArray[counter + round*16] ^ pad).to_bytes(1, 'little') + mutatedBytes

                for correctByte in range(0, 256): #should use ascii.printable range
                    mutatedCipherByte = (encrypted[pos-16] ^ correctByte ^ pad).to_bytes(1, 'little')

                    wholeMutatedCipherBytes = mutatedCipherByte + mutatedBytes

                    mutatedCipherText = encrypted[0:pos-16] + wholeMutatedCipherBytes + encrypted[(16*(blocksOfCipherText-1)):(16*blocksOfCipherText)]

                    # server will do this part for us
                    decrypted = aesCBCgiven(key,iv,mutatedCipherText, 'd')


                    if(decrypted != "Padding error bitch!"):
                        # print(mutatedCipherText)
                        # print("ASCII value: " ,chr(correctByte))
                        if(round >= 0 and pad == 0x01):
                            possibleValues.append(correctByte)
                            # print('\033[92m' + "correctByte: "+ '\033[0m', correctByte.to_bytes(1, 'little'), pad, round)
                        else:
                            correctByteArray.append(correctByte)

                #edge case of solving last byte check of the padding block
                if(round >= 0 and pad == 0x01):
                    if(len(possibleValues) == 1):
                        correctByteArray.append(possibleValues[0])
                    else:
                        correctByteArray.append(possibleValues[len(possibleValues)-1])

                pos = pos - 1

            blocksOfCipherText = blocksOfCipherText - 1

        flag = b''
        for i in correctByteArray:
            flag = i.to_bytes(1, 'little') + flag

        print("Our flag: ", flag[0:plainTextLength-16])
        print("Plaintext:", plainText[16:])

        if(flag[0:plainTextLength-16] == plainText[16:]):
            print("flag is correct")
        else:
            print("flag is wrong bro")
