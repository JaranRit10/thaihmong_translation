

if __name__ == '__main__':
    import time
    bb = {"เรา":"peb","เรา":"peb","เรา2":"peb","เรา3":"peb"}
    for i in range(1000):
        bb[i]= i+2
        if(len(bb) >800):
            print("bb(clear)",bb)
            bb.clear()

        print(bb)
    time.sleep(2)
    bb.clear()
    print('clear all')