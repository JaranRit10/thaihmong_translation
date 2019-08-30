import threading

def worker(number):
    print("I am thread : "+str(number))

thread_list = []

for i in range(4):
    thread = threading.Thread(target=worker,args=(i,))
    thread_list.append(thread)
    thread.start()