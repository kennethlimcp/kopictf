#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Lim Chen Pin Kenneth
# 28 March 2017
# Client starter code for challenge
# Pair programmed with Ryan Lim

import socket

if __name__ == "__main__":
	# NOTE: UPPERCASE names for constants is a (nice) Python convention
	URL = 'localhost'
	PORT = 1337

	cipherText = b'P\xe2s\x14&o\xda\x04\x124\xb3\xf2\x8d\x97\xeaG\xa4H\n5}m\t.\xe1\xaf\xa7\x0f\xc3\x8d8\x04!\x06AP\x13\xa8[\x01#\xcao\xb9\xc6\xbf^\x97*A\x92j)MfmEL\xa5\xef\xbc.(\xfe\xc2\xf1\xb3e@Z\x91=\x19\xba\xdc\xbb\x1a\x01Eu'

	decryptedByteArray = []
	bytesInCipherText = len(cipherText)
	blocksOfCipherText = int(bytesInCipherText / 16)

	#connect to server
	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	conn.connect ((URL,PORT))


	#send your ciphertext (as bytes) to the Oracle
	conn.send(cipherText)
	serverResult = conn.recv(7)
	print(serverResult.decode('utf-8'))
	conn.close()

