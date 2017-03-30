#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 26 March 2017
# Full solution proof of concept
# Pair programmed with Ryan Lim

from aesCBC import aesCBC
import os, sys, time

class bcolors:
    HEADER = '\033[95m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printStatus(correctByte, block, front, mutatedCipherByte, mutatedBytes, back):
    time.sleep(0.1)
    sys.stdout.write("\r" + bcolors.OKGREEN + "[+] " + bcolors.ENDC + "Test [Byte " + str(correctByte) + "/256]- Block - " + str(block) + "   " + str(front) + bcolors.YELLOW + str(mutatedCipherByte) + bcolors.ENDC + bcolors.RED + str(mutatedBytes) + bcolors.ENDC)
    sys.stdout.flush()

def printFoundByte(correctByteArray):
    # time.sleep(0.1)

    result = b''
    for i in correctByteArray:
        result = i.to_bytes(1, 'little') + result

    print("")
    print(bcolors.OKGREEN + "[+] " + bcolors.ENDC, "Found ", len(correctByteArray), " Byte: ", result)
    print("")

if __name__=="__main__":
    print("Starting attack :)")

    iv =  str.encode("1234567890123456")
    key =  str.encode("1234567890123456")
    # 2 blocks of repeating "1234567890123456" string + "123456789012345"
    # plainText =  str.encode("12345678901234561234567890123456123456789012345")
    # plainText =  str.encode("1234567890123456ABCDEFGHIJKLMNOP1234567890123456abcdefghjklmnop")
    # plainText =  str.encode("12345678901234561234567890123456123456789012345")

    plainText = os.urandom(62)
    encrypted = aesCBC(key,iv,plainText, 'e')
    decrypted = aesCBC(key,iv,encrypted, 'd')

    print("plaintext:          ", plainText)
    print("encypted:           ", encrypted)
    print("decrypted:          ", decrypted)

    if(plainText == decrypted):
      print ("plaintext == decrypted")
    else:
      print("error")

    print("\n\nPerforming mutation attack")

    for plainTextLength in range(16*3, 16*100):
        print("plainTextLength", plainTextLength)

        plainText = os.urandom(plainTextLength)
        encrypted = aesCBC(key,iv,plainText, 'e')

        correctByteArray = []
        bytesInCipherText = len(encrypted)
        blocksOfCipherText = int(bytesInCipherText / 16)

        pos = bytesInCipherText - 1

        for round in range(blocksOfCipherText-1):
            # print("pos", pos)
            possibleValues = []

            for pad in range(1,17):
                printFoundByte(correctByteArray)

                mutatedBytes = b''
                # print("pad", pad)
                if(pad > 1):
                    for counter in range(0, pad-1):
                        mutatedBytes = (encrypted[((blocksOfCipherText-1)*16)-1-counter] ^ correctByteArray[counter + round*16] ^ pad).to_bytes(1, 'little') + mutatedBytes

                for correctByte in range(0, 256): #should use ascii.printable range

                    mutatedCipherByte = (encrypted[pos-16] ^ correctByte ^ pad).to_bytes(1, 'little')

                    wholeMutatedCipherBytes = mutatedCipherByte + mutatedBytes

                    mutatedCipherText = encrypted[0:pos-16] + wholeMutatedCipherBytes + encrypted[(16*(blocksOfCipherText-1)):(16*blocksOfCipherText)]

                    printStatus(correctByte,blocksOfCipherText, encrypted[0:pos-16], mutatedCipherByte, mutatedBytes, encrypted[(16*(blocksOfCipherText-1)):(16*blocksOfCipherText)])


                    # server will do this part for us
                    try:
                        decrypted = aesCBC(key,iv,mutatedCipherText, 'd')
                        if(round >= 0 and pad == 0x01):
                            possibleValues.append(correctByte)
                        else:
                            correctByteArray.append(correctByte)
                    except ValueError as e:
                        pass

                #edge case of solving last byte check of the padding block with padding 0x01
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
