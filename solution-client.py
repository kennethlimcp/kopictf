#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA 2017

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: sudo pip3 install git+https://github.com/arthaud/python3-pwntools.git

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

#from pwn import remote
import socket
from aesCBC import aesCBC
import time

if __name__ == "__main__":
  # NOTE: UPPERCASE names for constants is a (nice) Python convention
  URL = 'localhost'
  PORT = 1337

  # iv =  str.encode("1234567890123456")
  # key =  str.encode("1234567890123456")
  #
  # plainText =  str.encode("IrrelevantStart!limkopiCTF{ReyonTheShark}<--flagnotaflaglol:))))")

  # encrypted = aesCBC(key,iv,plainText, 'e')
  # decrypted = aesCBC(key,iv,encrypted, 'd')

  conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  conn.connect ((URL,PORT))
  encrypted = conn.recv(4000).strip()
  print(encrypted)
  conn.close()

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
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect ((URL,PORT))
        message = conn.recv(1024)

        mutatedCipherByte = (encrypted[pos-16] ^ correctByte ^ pad).to_bytes(1, 'little')

        wholeMutatedCipherBytes = mutatedCipherByte + mutatedBytes

        mutatedCipherText = encrypted[0:pos-16] + wholeMutatedCipherBytes + encrypted[(16*(blocksOfCipherText-1)):(16*blocksOfCipherText)]

        # server will do this part for us
        # decrypted = aesCBC(key,iv,mutatedCipherText, 'd')
        conn.send(mutatedCipherText)
        serverResult = conn.recv(7)

        if(str(serverResult, 'utf-8') == "correct"):
          if(round >= 0 and pad == 0x01):
            possibleValues.append(correctByte)
          else:
            correctByteArray.append(correctByte)

        conn.close()

      #edge case of solving last byte check of the padding block
      if(round >= 0 and pad == 0x01):
        if(len(possibleValues) == 1):
          correctByteArray.append(possibleValues[0])
        else:
          correctByteArray.append(possibleValues[len(possibleValues)-1])

      pos = pos - 1
      solution = b''
      for i in correctByteArray:
        solution = i.to_bytes(1, 'little') + solution
      print(solution)


    blocksOfCipherText = blocksOfCipherText - 1
