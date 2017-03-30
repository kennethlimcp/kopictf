#!/usr/bin/env python3
# based on https://pymotw.com/2/socketserver/
# 50.020 Security Server Lab2
# Nils, SUTD, 2017


# Server for Team Reyon
# Requires: pip3 install pycrypto

import logging
import sys
import socketserver
import random
import string
import socket
import threading
import os
from aesCBC import aesCBC

port1 = 1337

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
        try:
            self.logger.debug('handle' + str(self.request.getsockname()))
            port = self.request.getsockname()[1]

            mess = "Please enter ciphertext :D\n"

            data = self.request.recv(16*10).strip() # including newline

            #Process user input as bytes
            ct_bytes = data
            self.logger.debug(ct_bytes.hex())

            decryptAttempt = aesCBC(key,iv,ct_bytes, 'd')
            self.request.send("ree".encode('ascii'))

        except ValueError as e:
            self.request.send('yon'.encode('ascii'))

        except:
            self.request.send('yon'.encode('ascii'))
            self.logger.debug("Error exception")

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
    iv =  b'~\x13\xbd\xd5\x9d\xb7\x9bw\x0b\xbe\xef\\u\xb47E'
    key = b'"]/\xfb}\x18V\xab\xf3\x1eY\x15\xef\xa5hH'

    address1 = ('0.0.0.0', port1)
    server1 = EchoServer(address1, EchoRequestHandler)

    t1 = threading.Thread(target=server1.serve_forever)
    t1.setDaemon(True)  # don't hang on exit
    t1.start()
    input("press a key to kill")
    t1.socket.close()
