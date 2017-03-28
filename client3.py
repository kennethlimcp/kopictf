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

if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = 'localhost'
    PORT = 1337
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect ((URL,PORT))
    # NOTE: conn is the connection handler
    #conn = remote(URL, PORT)
    
    # NOTE: try to use sendline()
    # conn.sendline("GET /\r\n\r\n")

    message = conn.recv(1024)
    # NOTE: try to use recvuntil() with different delimiters ...
    # DELIMITER = ' '
    # message = r.recvuntil(DELIMITER)
    # NOTE: now try to use recv()
    # message = conn.recv()
    #print("received message: {}".format(message))
    print(message.decode('ascii'))
    conn.send(bytes.fromhex('5cd47e1087e0b15e210925b3c003c3ade523f97af36837f18e07fe954cdba02148238560721efe294ae39f6ab5578d7f57e933c1ff5dde595b00f3cf629aaac7'))
    message = conn.recv(1024)
    print(message.decode('ascii'))

    conn.close()

