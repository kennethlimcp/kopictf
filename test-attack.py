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

    for correctByte in range(0, 256):
        mutatedCipherBlock = encrypted[0:-1] + (correctByte ^ 1).to_bytes(1, 'little')
        decrypted = aesCBCgiven(key,iv,mutatedCipherBlock, 'd')

        if(plainText == decrypted):
            print("mutated encyption:  ", mutatedCipherBlock)
            print("decrypted:          ", decrypted)
            print("correctByte", correctByte, hex(correctByte), hex(correctByte ^ int.from_bytes(encrypted[-1:], 'little')))
            exit()
