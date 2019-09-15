

if __name__ == '__main__':
    a= "เราไปแล้วทำไม"
    b = a.find(" ")
    print(b)
    if(b != -1):
        a = list(a)
        a[b]=','
        a = "".join(a)
    print(a)