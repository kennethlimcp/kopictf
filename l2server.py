#!/usr/bin/env python3
# based on https://pymotw.com/2/socketserver/
# 50.020 Security Server Lab2
# Nils, SUTD, 2017

import logging
import sys
import socketserver
import random
import string
import socket
import threading
import os
from aesCBC import aesCBC
from Padding import *

port1 = 1337
CIPHERTEXT_BYTELENGTH = 16*5

logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )


class EchoRequestHandler(socketserver.BaseRequestHandler):

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        socketserver.BaseRequestHandler.__init__(
            self, request, client_address, server)
        return

    def handle(self):
        self.logger.debug('handle' + str(self.request.getsockname()))
        port = self.request.getsockname()[1]

        mess = "Please enter ciphertext :D\n"

        # self.request.send(mess.encode('ascii'))
        self.request.send(encrypted)
        data = self.request.recv(16*50).strip() # including newline

        #Process user input as bytes
        ct_bytes = data
        self.logger.debug(ct_bytes.hex())
        try:
            decryptAttempt = aesCBC(key,iv,ct_bytes, 'd')
            self.logger.debug(decryptAttempt==decrypted)
            self.request.send("correct".encode('ascii'))

        except ValueError as e:
            self.request.send('error'.encode('ascii'))

        #self.logger.debug('Your ciphertext was: ' + ct_bytes)
        # self.request.send('Goodbye!\n'.encode('ascii'))
        return


class EchoServer(socketserver.ThreadingMixIn,socketserver.TCPServer):

    def __init__(self, server_address, handler_class=EchoRequestHandler):

        self.logger = logging.getLogger('EchoServer')

        self.logger.debug('__init__')
        self.allow_reuse_address = True
        self.daemon_threads = True
        self.timeout = 3
        socketserver.TCPServer.__init__(self, server_address, handler_class)
        return

    def serve_forever(self):
        self.logger.debug('waiting for request')
        self.logger.info('Handling requests, press <Ctrl-C> to quit')
        while True:
            self.handle_request()
        return


if __name__ == '__main__':

    iv =  str.encode("1234567890123456")
    key =  str.encode("1234567890123456")

    plainText =  str.encode("IrrelevantStart!limkopiCTF{ReyonTheShark}<--flagnotaflaglol:))))")

    encrypted = aesCBC(key,iv,plainText, 'e')
    print (encrypted)
    decrypted = aesCBC(key,iv,encrypted, 'd')

    address1 = ('0.0.0.0', port1)
    server1 = EchoServer(address1, EchoRequestHandler)

    t1 = threading.Thread(target=server1.serve_forever)
    t1.setDaemon(True)  # don't hang on exit
    t1.start()
    input("press a key to kill")
    t1.socket.close()


 # mess = "Welcome to challenge \"%s\" of length %d: " % (
            # challenges[port]['text'], len(challenges[port]['data']))
            # footer = "\nPlease send your solution of length %d now:\n"%len(challenges[port]['data'])
            # self.request.send(mess.encode('ascii'))
            # self.request.send(challenges[port]['data'])
            # self.request.send(footer.encode('ascii'))
            # print("waiting for response of len %d"%len(challenges[port]['data']))
            # buf=b''
            # new= self.request.recv(10)
            # while len(buf)<len(challenges[port]['data']) and new  and not b'exit' in new:
            #     buf += new

            #     mis = len(challenges[port]['data'])-len(buf) # the number of bytes missing
            #     if mis > 10:
            #         mis = 10 # we don't want to wait for too long?
            #     new = self.request.recv(mis)
            # self.logger.debug('recv()->"%s"', buf)
            # print("received response of len %d"%len(buf))
            # data=buf[:len(challenges[port]['data'])]
            # val = challenges[port]['val'](data, challenges[port]['sol'].encode('ascii'), challenges[port]['key'].encode('ascii'))
            # if val:
            #     self.request.send(val)
            # else:
            #     self.request.send('Incorrect answer, please try again\n'.encode('ascii'))
