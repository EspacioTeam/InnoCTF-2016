#!/usr/bin/python2
import logging
import multiprocessing as mp
import socket
import threading
import time
import hashlib
import random
import sys

logger = mp.log_to_stderr(logging.DEBUG)


def chash(x, algorithm):
    obj = hashlib.new(algorithm)
    obj.update(x)
    return obj.hexdigest()


def level(i, client, address):
    alphabet = b"abcdefghijklmnopqrstuvwxyz" + b"1234"
    s = "".join([random.choice(alphabet) for x in range(21)]) 

    algorithms = list(hashlib.algorithms_available)
    Q = random.randint(0, len(algorithms)-1)
    h = chash(s, algorithms[Q])
    client.send("\nLevel "+str(1+i)+"/5.\nSend us a string starting with "+ s[:16] +", ^[1-4a-z]{21}$, such that its "+ algorithms[Q] +" hashsum equals to "+h+". And... you have 60 seconds.\n")
    
    # receive answer
    answer = client.recv(23) # 21 + \r\n
    if chash(answer[:21], algorithms[Q]) == h:
        client.send("correct!\n")
        logger.debug("{0} passed {1} level. ".format(address, i+1))
        return True
    else:
        raise socket.timeout("died")


class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.died = "##################\n" + "#" + " "*16 +"#\n#    YOU DIED    #\n#" + " "*16 + "#\n##################\n"

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        logger.debug("{0} connected. ".format(address))

        try:
            client.send("Welcome. You want to defuse the hashbomb, isn't it? So. You actually have to defuse 5 bombs. Are you ready?")
            for i in range(5): # no of rounds
                level(i, client, address)
            client.send("\n... defused... your flag: " + str(FLAG))
            logger.debug("{0} got flag. ".format(address))
            client.close()
        except socket.timeout as tout:
            client.send(self.died)
            client.close()
            logger.debug("{0} died. ".format(address))
            return False
        except Exception as e:
            print(e) # for debug
            client.close()
            logger.debug("{0} disconnected. ".format(address))
            return False

if __name__ == "__main__":
    global FLAG

    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    else:
        PORT = 50001

    with open("flag.txt", "rb") as r:
        FLAG = r.read()

    ThreadedServer('0.0.0.0', PORT).listen()