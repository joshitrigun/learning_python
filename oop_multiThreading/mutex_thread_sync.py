from threading import *
from time import *


def display(str):
    l.acquire()
    for x in str:
        print(x)
    l.release()

l = Semaphore(2)

t1 = Thread(target=display, args=('HELLO WORLD',))
t2 = Thread(target=display, args=('you are welcome',))
t3 = Thread(target=display, args=('123456798',))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()