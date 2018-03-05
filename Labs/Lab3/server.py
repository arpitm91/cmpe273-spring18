import zmq
import time
from threading import Thread
from queue import Queue


def inputing(q):
    context1 = zmq.Context()
    sock1 = context1.socket(zmq.REP)
    sock1.bind("tcp://127.0.0.1:5678")
    while True:
        message1 = str(sock1.recv().decode())
        sock1.send_string("Echo: " + message1)
        q.put(message1)

def broadcasting(q):
    context = zmq.Context()
    sock = context.socket(zmq.PUB)
    sock.bind("tcp://127.0.0.1:5680")
    while True:
        while q.qsize() != 0:
            current_message = q.get()
            sock.send_string(current_message)
            q.task_done()

q = Queue(maxsize=0)

inputin = (Thread(target=inputing, args=(q, )))
inputin.start()

broadcast = (Thread(target=broadcasting, args=(q, )))
broadcast.start()

