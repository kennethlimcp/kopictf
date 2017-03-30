#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Lim Chen Pin Kenneth
# 28 March 2017
# Client solution for challenge
# Pair programmed with Ryan Lim

import socket

if __name__ == "__main__":
  # NOTE: UPPERCASE names for constants is a (nice) Python convention
  URL = 'localhost'
  PORT = 1337

  encrypted = b"P\xe2s\x14&o\xda\x04\x124\xb3\xf2\x8d\x97\xeaG\x1fn9%\x8c\xb8\xb6'K\xdd6\xdc>IZ\x95\xf5?\xd1CM\xd5\xe1r\xaf\x04+\xed5\xda&\xe6\xc3\x84\xf2\xc9\xc5rx\n_\xb7*\xd8\xa8\x9f\xb9a"


  # conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # conn.connect ((URL,PORT))
  # encrypted = conn.recv(4000).strip()
  # print("\nCipher text received: " encrypted, "\n\n")
  # conn.close()

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

      for correctByte in reversed(range(256)): #should use ascii.printable range
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect ((URL,PORT))

        mutatedCipherByte = (encrypted[pos-16] ^ correctByte ^ pad).to_bytes(1, 'little')

        wholeMutatedCipherBytes = mutatedCipherByte + mutatedBytes

        mutatedCipherText = encrypted[0:pos-16] + wholeMutatedCipherBytes + encrypted[(16*(blocksOfCipherText-1)):(16*blocksOfCipherText)]

        # server will do this part for us
        conn.send(mutatedCipherText)
        serverResult = conn.recv(7)

        if(str(serverResult, 'utf-8') == "ree"):
          # if(round >= 0 and pad == 0x01):
            # possibleValues.append(correctByte)
          # else:
          correctByteArray.append(correctByte)

        conn.close()

      #edge case of solving last byte check of the padding block
      # if(round >= 0 and pad == 0x01):
      #   if(len(possibleValues) == 1):
      #     correctByteArray.append(possibleValues[0])
      #   else:
      #     correctByteArray.append(possibleValues[len(possibleValues)-1])

      pos = pos - 1
      solution = b''
      for i in correctByteArray:
        solution = i.to_bytes(1, 'little') + solution
      print(solution)


    blocksOfCipherText = blocksOfCipherText - 1
