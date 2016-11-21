#!/usr/bin/python3
import socket
import threading
import random
import csv

#words = genfromtxt('words.csv', delimiter=',',dtype='str')
words = []
csv.register_dialect('unixpwd', delimiter=',', quoting=csv.QUOTE_NONE)
with open('./words.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        words.append(row)
answers = [u"СЪЕДОБНОЕ", u"НЕСЪЕДОБНОЕ"]
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(500)
        while True:
            client, address = self.sock.accept()
            client.settimeout(500)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        count = 0
        size = 60
        print("%s: connected" % address[0])
        while True:
            # word sending
            word = random.choice(words)
            print(word[0])
            client.send(bytearray(word[0].encode('utf-8')))
            answer = answers[0] if word[1] == "t" else answers[1]
            try:
                data = client.recv(size).decode('utf-8')
                if data:
                    if(data.upper() == answer.upper()):
                        count += 1
                        if(count == 500):
                            client.send(b'InnoCTF{Gr347_5ucc355!_y0u_4r3_w1n!_u53_7h1s_fl4g}')
                            client.close()
                            break
                    else:
                        client.send(b'FAIL. TRY AGAIN')
                        client.close()
                        break
                    print("%s: %s %d" % (address[0], data, count))
                else:
                    raise error('Client disconnected')
            except IOError as e:
                print ("I/O error({0}): {1}".format(e.errno, e.strerror))
                print("%s: disconnected" % address[0])
                client.close()
                return False

if __name__ == "__main__":
    port_num = 47139
    ThreadedServer('',port_num).listen()
