import SocketServer
import thread

dev = pixet.devices()[0]  # get first device
aborting = False

class EchoRequestHandler(SocketServer.BaseRequestHandler):

    def setup(self):
        """ when new client connets"""

        print("Client: %s, %s" % (self.client_address, "connected!"))

    def handle(self):
        """ Main loop for TCP/IP communication with client. Reads data from client
            and if it is a command process it and pass it to processCommand function"""

        if aborting:
            return

        data = 'dummy'
        while data:
            if aborting:
                return

            # receive data from client
            data = self.request.recv(1024)
            data = data.strip()
            print(data)

            # if quit, stop the loop
            if data.strip() == "QUIT()":
                return

            # if it is a command - has bracket, parse arguments
            if "(" in data:
                items = data.split("(")
                cmd = items[0]
                params = items[1][:-1]
                params = [x.strip() for x in params.split(",")]
                res = self.processCommand(cmd, params)
                try:
                    self.request.send(res + "\n")
                except:
                    print("exception")


    def processCommand(self, cmd, params):
        """ Processing command received from client"""

        cmd = cmd.upper()
        res = "ERR Unknown Command"

        if cmd == "START":
            res = self.cmdStart(params)
        if cmd == "IS_RUNNING":
            res = self.cmdIsRunning(params)

        return res

    def cmdStart(self, params):
        acqCount = int(params[1])
        acqTime = float(params[3])
        rc = dev.doSimpleAcquisition(acqCount, acqTime, 0, "")
        return "OK" if rc == 0 else "ERROR"

    def cmdIsRunning(self, params):
        return "YES" if dev.isAcquisitionRunning() else "NO"

    def finish(self):
        """ Client diesconnected """

        print("Client: %s %s" % (self.client_address, "disconnected!"))


# kill the server
def exitCallback(value):
    global server
    print("Exit")
    server.server_close()

# when abort pressed stop the server
def onAbort():
    global aborting
    global server
    aborting = True
    def kill(server):
        server.shutdown()
        server.server_close()
    thread.start_new_thread(kill, (server,))
    print("Aborted")


# create server and run it
server = SocketServer.ThreadingTCPServer(('', 59876), EchoRequestHandler)
pixet.registerEvent("Exit", exitCallback, exitCallback)
server.serve_forever()
server.server_close()
