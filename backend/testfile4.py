
import multiprocessing as mp
import time

def job(sentence):
    for i in range(4):
        time.sleep(1)
        print(f"{sentence} translated")

if(__name__=='__main__'):
    pp = []
    sentence =["เราไปทำงาน","สวัสดีชาวโลกทุกคน"]
    s = time.time()
    for j in sentence:
        p = mp.Process(target=job,args=(j,))
        p.start()
        pp.append(p)
    print('เริ่มงานได้แล้ว')
    for p in pp:
        p.join()
    print('เก็บกวาดหลังเลิกงาน',time.time()-s)