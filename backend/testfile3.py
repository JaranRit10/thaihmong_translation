
import threading
import time

def sleeper(n,name):
    print(f"{name} sleep 5 minut")
    time.sleep(n)
    print("wake up")

t = threading.Thread(target=sleeper,name='thread1',args=(5,"thread1"))
t = threading.Thread(target=sleeper,name='thread1',args=(5,"thread1"))

t.start()
t.join()

print("\nhello")
print("\nhello6")
