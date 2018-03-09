import zmq
import sys
from threading import Thread

ME = sys.argv[1]

def outputting():
    context = zmq.Context()
    sock = context.socket(zmq.REQ)
    sock.connect("tcp://127.0.0.1:5678")

    while 1:
        sock.send_string("["+ME+"]:" + input("["+ME+"]>"))
        mess= (sock.recv().decode())

def receiving():
    context = zmq.Context()
    sock = context.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, "")
    sock.connect("tcp://127.0.0.1:5680")

    while True:
        message= sock.recv().decode()
        if message.find("["+ME+"]:") != 0:
            print("\n"+message+"\n["+ME+"]>", end="")
            

print("User["+ME+"] Connected to the chat server.")

output = (Thread(target=outputting, args=( )))
output.start()

receive = (Thread(target=receiving, args=( )))
receive.start()
