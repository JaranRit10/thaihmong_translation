from multiprocessing import Pool
import time


class C:
    def f(self, name):
        time.sleep(1)
        return ('hello %s,' % name)



    def run(self,tt):
        pool = Pool(processes=2)
        a = pool.map(self.f, tt)
        return a


if __name__ == '__main__':
    s = time.time()
    c = C()
    d= c.run(('frank', 'justin', 'osi', 'thomas'))
    print(d ,time.time()-s)