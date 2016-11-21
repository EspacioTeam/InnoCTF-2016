import socket
import threading
import random
tmp = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(50)
        while True:
            client, address = self.sock.accept()
            client.settimeout(500) # for debugging. 1 sec for release
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        count = 0
        size = 10
        print("%s: connected" % address[0])
        while True:
            # file sending
            let = random.choice(tmp)
            f = open("img/%s-min.png" % let, "rb")
            img = f.read(4096)
            print(let)
            client.send(img)
            f.close
            try:
                data = client.recv(size).decode("utf-8")
                if data:
                    if(data == let):
                        count += 1
                        if(count == 500): #for debugging. 500 for release
                            print("tut")
                            client.send(b'InnoCTF{Unc13_54m_d035_th3_b35t_h3_c4n}')
                            client.close()
                            break
                    else:
                        client.send(b'FAIL. TRY AGAIN')
                        client.close()
                        break
                    print("%s: %s %d" % (address[0], data, count))
                else:
                    raise error('Client disconnected')
            except:
                print("%s: disconnected" % address[0])
                client.close()
                return False

if __name__ == "__main__":
    port_num = 31265
    ThreadedServer('',port_num).listen()
