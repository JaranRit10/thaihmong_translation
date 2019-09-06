from backend.testfile3 import C
import time
class a:
    pass

if __name__ == '__main__':
    tt = C()
    s = time.time()
    ss = tt.run(('frank', 'justin', 'osi', 'thomas'))
    print(ss ,time.time()-s)