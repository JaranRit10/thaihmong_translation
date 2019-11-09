text = """
ฉันก็เหมือนกัน ฉันมีนัดกับเพื่อน	0
วันนี้เป็นวันอะไร 0
วันนี้วันที่เท่าไร	0
มีอะไรให้ช่วยไหม    0
คุณต้องการสีไหนค่ะ	0
ตัวนี้สวยมากเลยค่ะ	0
ขอลองสวมหน่อยได้ไหมครับ	0
สวมพอดีไหมค่ะ	0
คุณมีตัวใหญ่กว่านี้ไหมครับ	0
ราคาเท่าไรครับ	0
ราคานี้เป็นราคาที่ลดแล้วค่ะ	0
ตกลง ผมเอาตัวนี้ครับ	0

    """

quention = ['เป็นอย่างไงบ้าง', 'อย่างไง','แล้วคุณล่ะ','คุณล่ะ','ได้ไหม','ไหม','ที่ไหน','คุณล่ะ','อะไร','เท่าไหร่','ยังไง',
            'เท่าไร','เมื่อไหร่','อย่างไร','เป็นใคร','หรือเปล่า','กี่','ไหน']
sentence_ = text.splitlines()
count = 0
number = []
for sentence in sentence_:
    sentence = sentence.strip()
    if (sentence != ''):
        count += 1
        check = False
        for q in quention:
            if (q in sentence):
                # print(q in sentence)
                number.append(1)
                check = True
                break;
        if(check == False):
            number.append(0)

print("lise number :",number)
for n in number:
    print(n)
print("number of sentence : ",count)
