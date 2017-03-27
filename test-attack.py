#!/usr/bin/env python3
# Lim Chen Pin Kenneth
# 26 March 2017
# Attack test code

from aesCBCgiven import aesCBCgiven

if __name__=="__main__":
    print("Starting attack :)")

    iv =  str.encode("1234567890123456")
    key =  str.encode("1234567890123456")
    # 2 blocks of repeating "1234567890123456" string + "123456789012345"
    plainText =  str.encode("12345678901234561234567890123456123456789012345")

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

    guessedPlainText = ""

    #2nd last byte
    for correctByte in range(0, 256):
        mutatedCipherByte = encrypted[14] ^ correctByte ^ 0x02 #XOR in int
        mutatedCipherByteStr = mutatedCipherByte.to_bytes(1, 'little') #convert to byte format

        mutatedCipherText = encrypted[0:14] + mutatedCipherByteStr + (encrypted[15]^54^0x02).to_bytes(1, 'little') + encrypted[16:32]

        decrypted = aesCBCgiven(key,iv,mutatedCipherText, 'd')

        if(decrypted != "Padding error bitch!"):
            print(mutatedCipherText)
            print("correctByte", correctByte)
            print("value: " ,chr(correctByte))
            guessedPlainText = chr(correctByte) + guessedPlainText

    exit()


    #last byte
    for correctByte in range(0, 256):
        mutatedCipherByte = encrypted[15] ^ correctByte ^ 0x01 #XOR in int
        mutatedCipherByteStr = mutatedCipherByte.to_bytes(1, 'little') #convert to byte format

        mutatedCipherText = encrypted[0:15] + mutatedCipherByteStr + encrypted[16:32]

        decrypted = aesCBCgiven(key,iv,mutatedCipherText, 'd')

        if(decrypted != "Padding error bitch!"):
            print(mutatedCipherText)
            print("correctByte", correctByte)
            print("value: " ,chr(correctByte))
            guessedPlainText = chr(correctByte) + guessedPlainText
