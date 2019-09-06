import  tltk.nlp
from multiprocessing import Pool
import time

class Grammar () :

    questionword = ['หรือเปล่า', 'หรือยัง', 'เปล่า', 'ไหม']
    list =[]
    def grammarHmong(self,Text):
        Text = Text.strip()
        tltk.nlp.pos_tag(Text)
        WordLst = tltk.nlp.word_segment(Text).split('|')
        # print("แบบ 2 : " + str(tltk.nlp.pos_tag_wordlist(WordLst)))
        self.list = tltk.nlp.pos_tag_wordlist(WordLst)

        print(self.list)
        # print(type(list))

        print("ผลลัพธ์เริ่มต้น : " + str(self.list))
        # ใช้เเช็คให้เข้าเงื่อนไขได้เพียงครั้งเดียว
        check=[True,True,True,True]

        # ใช้ตรวจสอบประโยคการแสดงความเป็นเจ้าของกับประโยคทที่มีการบอกลักษณะนาม
        for x in range(0, len(self.list) - 2):

            # ประโยคการแสดงความเป็นเจ้าของ มีคำว่าของ
            if (self.list[x][0] == "ของ" and self.list[x][1] != "NOUN" and check[0]== True):
                self.sentence1()
                self.complete()
                check[0] = False
            # ประโยคการแสดงความเป็นเจ้าของ ไม่มีคำว่าของ
            if (x <= len(self.list) - 2):
                    if (check[1] == True and self.list[x][1] == "NOUN" and self.list[x + 1][1] == "PRON"):
                        self.sentence1_1()
                        self.complete()
                        check[1] = False

            # ประโยคมีคำถาม
            if (check[2] == True and self.list[len(self.list)-2][0] in self.questionword ):
                self.sentence2()
                self.complete()
                check[2] = False
            # ประโยคทที่มีการบอกลักษณะนาม
            if (check[3] == True and self.list[x][1] == "NOUN" and self.list[x + 1][1] == "NUM" and self.list[x + 2][1] == "NOUN" ):
                self.sentence3()
                check[3] = 0
            elif (check[3] == True and self.list[x][1] == "NOUN" and (self.list[x + 1][1]) == "NOUN" and x <= len(self.list) - 2):
                self.sentence3()
                check[3] = 0
        print("ผลลัพธ์สุดท้าย : "+str(self.list))
        return  self.list

    # แสดงความเป็นเจ้าของ
    def sentence1(self):
        print("ประโยคเจ้าของ มีคำว่าของ")
        word_managed = set()
        for x in range(0, len(self.list) - 2):
            if(not x in word_managed):
                # ประโยคที่มีพ่อแม่มาเกี่ยวข้อง
                if (self.list[x][0]=="ของ" and (self.list[x+1][0]!="ของ" and self.list[x-1][0]!="ของ") ):
                    if (self.list[x][0] == "ของ" and (self.list[x - 1][0] == "พ่อแม่" or self.list[x - 1][0] == "แม่พ่อ")):
                        subject = self.list[x+1]
                        self.list.pop(x)
                        self.list.pop(x)
                        self.list.pop(x - 1)
                        self.list.insert(x - 1,('แม่', 'NOUN'))
                        word_managed.add(x-1)
                        self.list.insert(x - 1, subject)
                        word_managed.add(x - 1)
                        self.list.insert(x - 1, ('และ', 'CCONJ'))
                        word_managed.add(x - 1)
                        self.list.insert(x - 1, ('พ่อ', 'NOUN'))
                        word_managed.add(x - 1)
                        self.list.insert(x - 1, subject)
                        word_managed.add(x - 1)
                        print("ย่อย 1")

                    elif (self.list[x][0] == "ของ" and (self.list[x - 1][0] == "พ่อ" or self.list[x - 1][0] == "แม่")):
                        self.list[x - 1], self.list[x + 1] = self.list[x + 1], self.list[x - 1]
                        self.list.pop(x)
                        word_managed.add(x)
                        word_managed.add(x-1)
                        print("ย่อย 2")
                    elif (self.list[x][0] == "ของ" and (self.list[x - 1][1] == "VERB" or self.list[x - 1][1] == "DET" )):
                        self.list[x], self.list[x + 1] = self.list[x + 1], self.list[x]
                        word_managed.add(x+1)
                        word_managed.add(x)
                        print("ย่อย 3")
                    #วันที่สี่ของเดือนสิงหาคม
                    elif (self.list[x][0] == "ของ" and (self.list[x - 1][1] != "VERB" and self.list[x - 1][1] != "NUM") ):
                        if(self.list[x-1]==('<s/>', 'PUNCT')):
                            self.list[x],self.list[x+1] = self.list[x+1],self.list[x]
                            word_managed.add(x)
                            word_managed.add(x+1)
                            print("ย่อย 4.1")
                        else:
                            self.list.pop(x)
                            self.list.insert(x,('ของ', 'CLASS'))
                            self.list[x-1], self.list[x + 1] = self.list[x + 1], self.list[x-1]
                            word_managed.add(x + 1)
                            word_managed.add(x)
                            word_managed.add(x-1)
                            print("ย่อย 4.2")

    # แสดงความเป็นเจ้าของ ไม่มีคำว่าของ
    def sentence1_1(self):
        print("ไม่มีคำว่าของ")
        error_Word =['วันนี้']
        for x in range(0,len(self.list)-2):
            try: #เพราะบางครั้งอินเดชเกิน list[x][1] ตัดเป็น segment ก่อนแล้วเอาตัวหลังสุด
                if (self.list[x][1] == "NOUN" and self.list[x][1] == "วันนี้" and self.list[x + 1][1] == "PRON"):
                    self.list[x],self.list[x+1] = self.list[x+1],self.list[x]
                elif (self.list[x][1] == "NOUN" and self.list[x + 1][1] == "PRON" and (self.list[x][0] in error_Word)!=True):
                    self.list[x], self.list[x + 1] = self.list[x + 1], self.list[x]
            except Exception as e:
                print("Error funtion 1.1 :"+e)

    # ประโยคคำถาม
    def sentence2(self):
        print("ประโยคคำถาม")
        check = False
        for x in range(0,len(self.list)-2):
            if(self.list[x][1]=="VERB"):
                first =x
                self.list.insert(first, self.list[len(self.list) - 2])
                self.list.pop(len(self.list)-2)
                check = True
                break
        if(check==False):
            self.list[len(self.list)-2],self.list[len(self.list)-3] = self.list[len(self.list)-3] ,self.list[len(self.list)-2]

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
        for x in range(0,len(self.list)-2):
            try:
                if(not x in word_managed):
                    if(self.list[x][1]=="NOUN" and self.list[x+1][1]=="NUM" and self.list[x+2][1]=="NOUN" ):
                        word = (self.list[x + 2][0], "CLASS")
                        self.list.pop(x + 2)
                        self.list.insert(x + 2, word)
                        self.list.insert(x + 3,self.list[x])
                        self.list.pop(x)
                        word_managed.add(x)
                        word_managed.add(x+1)
                        word_managed.add(x+2)

                    if(self.list[x][1]=="NOUN" and self.list[x+1][1]=="NOUN" and
                    (self.list[x+1][0] in self.classifier)):
                        word = (self.list[x+1][0], "CLASS")
                        self.list.pop(x+1)
                        self.list.insert(x+1, word)
                        self.list[x],self.list[x+1] = self.list[x+1],self.list[x]
                        word_managed.add(x)
                        word_managed.add(x+1)
            except Exception as e:
                print(e )


    def complete(self):
        print("ผลลัพธ์ : " + str(self.list))

    def work(self,t):
        time.sleep(1)
        print(t)
        return t

    def theadRun(self,sentence):
        # pool = Pool(processes=2)
        # a = pool.map(self.f, tt)
        # return a

        pool = Pool(processes=2)
        get = pool.map(self.work,sentence)
        return get


if __name__ == '__main__':


        # tran = Grammar()
        # ss = time.time()
        # for i in range(4):
        #     word = "เราไปไหน"
        #     t = tran.grammarHmong(word)
        #     print("return : "+str(t))
        # print(time.time()-ss)



        tran = Grammar()
        ss = time.time()
        word = ["เราไปไหน1",]
        t = tran.theadRun(word)
        print("return : " + str(t))
        print(time.time()-ss)