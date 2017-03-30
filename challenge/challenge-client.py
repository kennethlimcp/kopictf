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

	encrypted = b';e\xc6\xd3\xb5\xed\xcaz\xd82\x97{`\x02\xd0\xee\xdf%\x18\xeaf\xaa/,\'3\xael\x83\xd9\xf2u\xda\'\xf5\xb0\xad"q\xfa\xf1\n\xecRZ?rh\x92{\x07\xaf@J4Y\xd2\x9a\xad9\xf0\xf4\x90\xf1'

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
