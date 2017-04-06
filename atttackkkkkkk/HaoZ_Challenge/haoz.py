from itertools import product
import string

def blockCipher(input, key):
    print("Decrypting one block")
    return input + int.from_bytes(key, 'little')


if __name__ == "__main__":
    print("Solving the Hao's challenge")

    # 128 bits
    iv = 0x09bf1e72affb6a192448a572e11e4620

    # Key is 3 character long, uppercase alphabetical
    # 24bits 3 byte long
    charList = string.ascii_uppercase
    keywords = [''.join(i) for i in product(charList, repeat = 3)]

    # First four bytes 0x25 0x50 0x44 0x46 (%PDF)

    inFile = open("secret.pdf", 'rb')
    inputData = inFile.read()

    inFile.close()

    for key in keywords:
        print("key", key)

        decrypted = blockCipher(iv, key)
        cipherText = int.from_bytes(inputData[0:16], 'little')

        print("decrypted", len(decrypted))
        print("cipherText", len(cipherText))

        plainText = decrypted ^ cipherText

        if(plainText == 0x25504446):
            print("Found match!")
            exit()

        exit()
