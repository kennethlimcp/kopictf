#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 26 March 2017
# Full solution proof of concept
# Pair programmed with Ryan Lim

from aesCBCgiven import aesCBCgiven
import os

if __name__=="__main__":
    print("Starting attack :)")

    iv =  str.encode("1234567890123456")
    key =  str.encode("1234567890123456")
    # 2 blocks of repeating "1234567890123456" string + "123456789012345"
    # plainText =  str.encode("12345678901234561234567890123456123456789012345")
    plainText =  str.encode("1234567890123456ABCDEFGHIJKLMNOP1234567890123456abcdefghjklmnop")

    # plainText = os.urandom(62)

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

    # encrypted = encrypted[0:48]

    correctByteArray = []
    bytesInCipherText = len(encrypted)
    blocksOfCipherText = int(bytesInCipherText / 16)

    pos = bytesInCipherText - 1


    for round in range(blocksOfCipherText-1):
        print("pos", pos)
        for pad in range(1,17):
            mutatedBytes = b''
            print("pad", pad)
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
                    print("correctByte: ", correctByte)
                    # print("ASCII value: " ,chr(correctByte))
                    correctByteArray.append(correctByte)

            pos = pos - 1

        blocksOfCipherText = blocksOfCipherText - 1

    flag = b''
    for i in correctByteArray:
        flag = i.to_bytes(1, 'little') + flag

    print("Our flag: ", flag[:-1], "\n\n")
    print(plainText[16:])

    #assertion only for padding or 01
    if(flag[:-1] == plainText[16:]):
        print("flag is correct")
    else:
        print("flag is wrong bro")
