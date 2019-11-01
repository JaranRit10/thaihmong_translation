
class a :
    global tt
    tt = 555
    def test(self,a):
        global tt
        print("A :",a,tt)
if __name__ == '__main__':
    bb = a()
    while(1):
        bb.test("b")

