from threading import *
from time import *


class MyData:
    def __init__(self):
        self.data = 0
        self.cv = Condition()

    def put(self, d):
        self.cv.acquire()
        self.cv.wait()
        self.data = d
        self.cv.notify()
        self.cv.release()
        sleep(0.5)

    def get(self):
        self.cv.acquire()
        self.cv.wait(timeout=0)
        x = self.data
        self.cv.notify()
        self.cv.release()
        sleep(0.5)
        return x


def producer(data):
    i = 1
    while True:
        data.put(i)
        print('producer', i)
        # sleep(0.5)
        i += 1


def consumer(data):
    while True:
        x = data.get()
        print('Consumer:', x)
        # sleep(0.5)


data = MyData()
t1 = Thread(target=lambda: producer(data))
t2 = Thread(target=lambda: consumer(data))

t1.start()
t2.start()

t1.join()
t2.join()
