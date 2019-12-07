

import threading

def a ():
    for i in range(50):
        print("A")

def b():
    for i in range(50):
        print("B")

cc = threading.Thread(target=a)
cc.start()

dd = threading.Thread(target=b)
dd.start()