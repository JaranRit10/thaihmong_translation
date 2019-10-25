import  tltk.nlp
from multiprocessing import Pool
import time

class Grammar () :

    notquestionword = ['ใช่']
    questionword = ['หรือเปล่า', 'หรือยัง', 'เปล่า', 'ไหม','หรือไม่']

    def grammarHmong(self,Text):
        global senten_list
        Text = Text.strip()

        commar = Text.find(" ")
        if (commar != -1):
            Text = list(Text)
            Text[commar] = ','
            Text = "".join(Text)

        tltk.nlp.pos_tag(Text)
        WordLst = tltk.nlp.word_segment(Text).split('|')
        # print("แบบ 2 : " + str(tltk.nlp.pos_tag_wordlist(WordLst)))
        senten_list = tltk.nlp.pos_tag_wordlist(WordLst)

        # print(list)
        # print(type(list))

        print("ผลลัพธ์เริ่มต้น : " + str(senten_list))
        # ใช้เเช็คให้เข้าเงื่อนไขได้เพียงครั้งเดียว
        check=[True,True,True,True]

        # ใช้ตรวจสอบประโยคการแสดงความเป็นเจ้าของกับประโยคทที่มีการบอกลักษณะนาม
        for x in range(0, len(senten_list) - 2):

            # ประโยคการแสดงความเป็นเจ้าของ มีคำว่าของ
            if (senten_list[x][0] == "ของ" and senten_list[x][1] != "NOUN" and check[0]== True):
                self.sentence1()
                self.complete()
                check[0] = False
            # ประโยคการแสดงความเป็นเจ้าของ ไม่มีคำว่าของ
            un_sentence = ['อะไร']
            if (x <= len(senten_list) - 2):
                    if (check[1] == True and senten_list[x][1] == "NOUN"
                            and senten_list[x + 1][1] == "PRON" and senten_list[x + 1][0] not in un_sentence):
                        self.sentence1_1()
                        self.complete()
                        check[1] = False

            # ประโยคมีคำถาม
            if (check[2] == True and senten_list[len(senten_list) - 2][0] in self.questionword):
                self.sentence2()
                self.complete()
                check[2] = False
            # ประโยคทที่มีการบอกลักษณะนาม
            if (check[3] == True and senten_list[x][1] == "NOUN" and senten_list[x + 1][1] == "NUM" and senten_list[x + 2][1] == "NOUN"):
                self.sentence3()
                check[3] = 0
            elif (check[3] == True and senten_list[x][1] == "NOUN" and (senten_list[x + 1][1]) == "NOUN" and x <= len(senten_list) - 2):
                self.sentence3()
                check[3] = 0
        print("ผลลัพธ์สุดท้าย : " + str(senten_list))
        return  senten_list

    # แสดงความเป็นเจ้าของ
    def sentence1(self):
        print("ประโยคเจ้าของ มีคำว่าของ")
        word_managed = set()
        for x in range(0, len(senten_list) - 2):
            if(not x in word_managed):
                # ประโยคที่มีพ่อแม่มาเกี่ยวข้อง
                if (senten_list[x][0]== "ของ" and (senten_list[x + 1][0] != "ของ" and senten_list[x - 1][0] != "ของ")):
                    if (senten_list[x][0] == "ของ" and (senten_list[x - 1][0] == "พ่อแม่" or senten_list[x - 1][0] == "แม่พ่อ")):
                        subject = senten_list[x + 1]
                        senten_list.pop(x)
                        senten_list.pop(x)
                        senten_list.pop(x - 1)
                        senten_list.insert(x - 1, ('แม่', 'NOUN'))
                        word_managed.add(x-1)
                        senten_list.insert(x - 1, subject)
                        word_managed.add(x - 1)
                        senten_list.insert(x - 1, ('และ', 'CCONJ'))
                        word_managed.add(x - 1)
                        senten_list.insert(x - 1, ('พ่อ', 'NOUN'))
                        word_managed.add(x - 1)
                        senten_list.insert(x - 1, subject)
                        word_managed.add(x - 1)
                        print("ย่อย 1")

                    elif (senten_list[x][0] == "ของ" and (senten_list[x - 1][0] == "พ่อ" or senten_list[x - 1][0] == "แม่")):
                        senten_list[x - 1], senten_list[x + 1] = senten_list[x + 1], senten_list[x - 1]
                        senten_list.pop(x)
                        word_managed.add(x)
                        word_managed.add(x-1)
                        print("ย่อย 2")
                    elif (senten_list[x][0] == "ของ" and (senten_list[x - 1][1] == "VERB" or senten_list[x - 1][1] == "DET")):
                        senten_list[x], senten_list[x + 1] = senten_list[x + 1], senten_list[x]
                        word_managed.add(x+1)
                        word_managed.add(x)
                        print("ย่อย 3")
                    #วันที่สี่ของเดือนสิงหาคม
                    elif (senten_list[x][0] == "ของ" and (senten_list[x - 1][1] != "VERB" and senten_list[x - 1][1] != "NUM")):
                        if(senten_list[x - 1]==('<s/>', 'PUNCT')):
                            senten_list[x], senten_list[x + 1] = senten_list[x + 1], senten_list[x]
                            word_managed.add(x)
                            word_managed.add(x+1)
                            print("ย่อย 4.1")
                        else:
                            senten_list.pop(x)
                            senten_list.insert(x, ('ของ', 'CLASS'))
                            senten_list[x - 1], senten_list[x + 1] = senten_list[x + 1], senten_list[x - 1]
                            word_managed.add(x + 1)
                            word_managed.add(x)
                            word_managed.add(x-1)
                            print("ย่อย 4.2")

    # แสดงความเป็นเจ้าของ ไม่มีคำว่าของ
    def sentence1_1(self):
        print("ไม่มีคำว่าของ")
        error_Word =['วันนี้']
        for x in range(0, len(senten_list) - 2):
            try: #เพราะบางครั้งอินเดชเกิน list[x][1] ตัดเป็น segment ก่อนแล้วเอาตัวหลังสุด
                if (senten_list[x][1] == "NOUN" and senten_list[x][1] == "วันนี้" and senten_list[x + 1][1] == "PRON"):
                    senten_list[x], senten_list[x + 1] = senten_list[x + 1], senten_list[x]
                elif (senten_list[x][1] == "NOUN" and senten_list[x + 1][1] == "PRON" and (senten_list[x][0] in error_Word) != True):
                    senten_list[x], senten_list[x + 1] = senten_list[x + 1], senten_list[x]
            except Exception as e:
                print("Error funtion 1.1 :"+e)

    # ประโยคคำถาม
    def sentence2(self):
        print("ประโยคคำถาม")
        check = False
        if(senten_list[len(senten_list)-2][0] in self.questionword and
                senten_list[len(senten_list)-3][0] =="ได้"):
            # สลับสองตำแหน่งหลัง
            senten_list[len(senten_list) - 2], senten_list[len(senten_list) - 3] = senten_list[len(senten_list) - 3],senten_list[len(senten_list) - 2]
            check = True
        else:
            for x in range(0, len(senten_list) - 2):
                if (senten_list[x][1] == "VERB" or senten_list[x][1] == "AUX"):
                    first = x
                    senten_list.insert(first, senten_list[len(senten_list) - 2])
                    senten_list.pop(len(senten_list) - 2)
                    check = True
                    break
        if(check==False):
            #สลับสองตำแหน่งหลังง
            senten_list[len(senten_list) - 2], senten_list[len(senten_list) - 3] = senten_list[len(senten_list) - 3] , senten_list[len(senten_list) - 2]



    classifier = ['รูป', 'ตัว', 'หลัง', 'พระองค์', 'องค์', 'ตน', 'ใบ', 'เรื่อง', 'สิ่ง', 'อัน', 'เลา', 'เชือก',
                  'เรือน', 'เล่ม', 'แท่ง', 'คน', 'กิ่ง', 'ขวด', 'ขอน', 'คัมภีร์', 'ฉบับ', 'ฉาก', 'ชุด',
                  'ดอก', 'ต้น', 'ไตร', 'นัด', 'นาย', 'เมล็ด', 'กอง', 'พวก', 'หมวด', 'หมู่', 'คณะ',
                  'ฝูง', 'นิกาย', 'สำรับ', 'โรง', 'วง', 'กลัก', 'กลุ่ม', 'ไขลง', 'คู่', 'เครือ', 'จั่น',
                  'ช่อ', 'แถว', 'แพ', 'แผ่น', 'ผืน', 'แถบ', 'บาน', 'ลูก', 'คัน', 'ลำ', 'ดวง',
                  'กระบอก', 'เส้น', 'สาย', 'ซี่', 'ตน']
    # ประโยคลักษณะนาม
    def sentence3(self):
        print("ประโยคที่มีลักษณะนาม")
        # สำหรับเก็บ index คำศัพท์ที่ถูกจัดการแล้ว
        word_managed = set()
        for x in range(0, len(senten_list) - 2):
            try:
                if(not x in word_managed):
                    if(senten_list[x][1]== "NOUN" and senten_list[x + 1][1]== "NUM" and senten_list[x + 2][1]== "NOUN"):
                        word = (senten_list[x + 2][0], "CLASS")
                        senten_list.pop(x + 2)
                        senten_list.insert(x + 2, word)
                        senten_list.insert(x + 3, senten_list[x])
                        senten_list.pop(x)
                        word_managed.add(x)
                        word_managed.add(x+1)
                        word_managed.add(x+2)

                    if(senten_list[x][1]== "NOUN" and senten_list[x + 1][1]== "NOUN" and
                    (senten_list[x + 1][0] in self.classifier)):
                        word = (senten_list[x + 1][0], "CLASS")
                        senten_list.pop(x + 1)
                        senten_list.insert(x + 1, word)
                        senten_list[x], senten_list[x + 1] = senten_list[x + 1], senten_list[x]
                        word_managed.add(x)
                        word_managed.add(x+1)
            except Exception as e:
                print(e )

    def complete(self):
        print("ผลลัพธ์ : " + str(senten_list))

if __name__ == '__main__':


        tran = Grammar()
        ss = time.time()
        for i in range(1):
            word = "เราไปไหนท"
            t = tran.grammarHmong(word)
            print("return : "+str(t))
        print(time.time()-ss)



        # tran = Grammar()
        # ss = time.time()
        # word = ["เราไปไหน","เราไปไหน","เราไปไหน","เราไปไหน"]
        # t = tran.theadRun(word)
        # print("return : " + str(t))
        # print(time.time()-ss)
        #
