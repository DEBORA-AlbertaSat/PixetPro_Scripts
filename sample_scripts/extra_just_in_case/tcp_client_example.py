import socket
import sys
import time

HOST = '127.0.0.1'
PORT = 59876

class Client(object):

    def __init__(self):
        super(Client, self).__init__()
        self.sock = None

    def open(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error, msg:
            sys.stderr.write("[ERROR] %s\n" % msg[1])
            sys.exit(1)

        try:
            self.sock.connect((HOST, PORT))
        except socket.error, msg:
            sys.stderr.write("[ERROR] %s\n" % msg[1])
            sys.exit(2)
        return self.sock

    def close(self):
        self.sock.close()

    def send(self, data):
        self.sock.send(data + "\r\n")

    def receive(self):
        try:
            self.sock.settimeout(0.5)
            return self.sock.recv(1024)
            self.sock.settimeout(None)
        except:
            return ""

    def startAcq(self):
        self.open()
        self.send("START(1,0.5)" % (time.time()))
        data = self.receive()
        self.close()
        return data

    def isRunning(self):
        self.open()
        self.send("IS_RUNNING()")
        data = self.receive().strip()
        self.close()
        print(data)
        return data == "YES"

c = Client()

for i in range(5):
    print("new acquisition")
    c.startAcq()

    time.sleep(1)
    while c.isRunning():
        print("running")
        time.sleep(0.5)

    print("finished")
