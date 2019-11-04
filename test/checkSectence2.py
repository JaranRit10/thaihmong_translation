text = """
คุณจะนั่งตรงไหน	0
ตกลงจะนั่งโต๊ะไหน	0
เชิญนั่งได้	0
คุณจะทานอะไรดี	1
วันนี้มีอะไรบ้าง	1
ร้านนี้มีอาหารอะไรอร่อยไหม	1

    """

detec = ['หน่อยได้ไหม','ฉันหน่อยว่า','ฉันหน่อยไหม','ฉันหน่อย','คุณหน่อย']
number = 0

sentence_ = text.splitlines()

new = []
for sentence in sentence_:
    sentence = sentence.strip()
    if(sentence!=''):
        get = sentence.split("\t")
        if(get[0]!=''):
            new.append(get)
print(new)
for i in range(len(new)):
    if(new[i][1]=='0'):
        print(new[i])

print("\n\n-----------------------\n")

for sen in new:
    print(sen[0],"\t",sen[1])