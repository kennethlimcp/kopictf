#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 26 March 2017
# Full solution proof of concept
# Pair programmed with Ryan Lim

from aesCBC import aesCBC
import os
import binascii

if __name__=="__main__":
    print("\n\nPerforming verification")

    iv =  str.encode("1234567890123456")
    key =  str.encode("1234567890123456")

    plainText =  str.encode("IrrelevantStart!limkopiCTF{ReyonTheShark}<--flagnotaflaglol:))))")

    encrypted = aesCBC(key,iv,plainText, 'e')
    decrypted = aesCBC(key,iv,encrypted, 'd')

    #perform assertion to check that our plainText is 4 blocks long, encrypted is 5 blocks due to padding
    assert len(plainText) == 16*4
    assert len(encrypted) == 16*5

    print("\nChecking with library enc/dec method\n")
    print("plaintext:          ", plainText)
    print("encypted:           ", encrypted)
    print("decrypted:          ", decrypted)

    if(plainText == decrypted):
      print ("plaintext == decrypted")
    else:
      print("error")

    print("\nChecking with our own solution method\n")

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
                try:
                    decrypted = aesCBC(key,iv,mutatedCipherText, 'd')
                    if(round >= 0 and pad == 0x01):
                        possibleValues.append(correctByte)
                    else:
                        correctByteArray.append(correctByte)
                except ValueError as e:
                    pass
                    # print("ValueError")
                # if(decrypted != "Padding error bitch!"):
                #     # print(mutatedCipherText)
                #     # print("ASCII value: " ,chr(correctByte))
                #     if(round >= 0 and pad == 0x01):
                #         possibleValues.append(correctByte)
                #         # print('\033[92m' + "correctByte: "+ '\033[0m', correctByte.to_bytes(1, 'little'), pad, round)
                #     else:
                #         correctByteArray.append(correctByte)

            #edge case of solving last byte check of the padding block
            if(round >= 0 and pad == 0x01):
                if(len(possibleValues) == 1):
                    correctByteArray.append(possibleValues[0])
                else:
                    correctByteArray.append(possibleValues[len(possibleValues)-1])

            pos = pos - 1

        blocksOfCipherText = blocksOfCipherText - 1

    solution = b''
    for i in correctByteArray:
        solution = i.to_bytes(1, 'little') + solution

    print("plaintext:          ", plainText)
    print("decrypted:          ", "xxxxxxxxxxxxxxx",solution[0:len(plainText)-16])

    assert solution[0:len(plainText)-16] == plainText[16:]

    if(solution[0:len(plainText)-16] == plainText[16:]):
        print ("plaintext == decrypted")
    else:
      print ("incorrection solution")

    print("\n\n")
