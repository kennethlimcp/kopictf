#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Lim Chen Pin Kenneth
# 28 March 2017
# Client solution for challenge
# Pair programmed with Ryan Lim

import socket

if __name__ == "__main__":
  # NOTE: UPPERCASE names for constants is a (nice) Python convention
  # URL = 'localhost'
  URL = "54.254.162.148"
  PORT = 1337

  encrypted = b';e\xc6\xd3\xb5\xed\xcaz\xd82\x97{`\x02\xd0\xee\xdf%\x18\xeaf\xaa/,\'3\xael\x83\xd9\xf2u\xda\'\xf5\xb0\xad"q\xfa\xf1\n\xecRZ?rh\x92{\x07\xaf@J4Y\xd2\x9a\xad9\xf0\xf4\x90\xf1'

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
          correctByteArray.append(correctByte)

        conn.close()

      pos = pos - 1
      solution = b''
      for i in correctByteArray:
        solution = i.to_bytes(1, 'little') + solution
      print(solution)

    blocksOfCipherText = blocksOfCipherText - 1
