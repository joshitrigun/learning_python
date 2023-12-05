from threading import *
from time import *
from queue import Queue

q = Queue()
def producer(que):
    i = 1
    while True:
        que.put(i)
        print('producer', i)
        sleep(0.5)
        i += 1


def consumer(que):
    while True:
        x = que.get()
        print('Consumer:', x)
        sleep(0.5)


t1 = Thread(target=lambda: producer(q))
t2 = Thread(target=lambda: consumer(q))

t1.start()
t2.start()

t1.join()
t2.join()
