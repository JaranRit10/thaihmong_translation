# Reading an excel file using Python
import openpyxl
import xlrd
from backend.Translate import Translate
import time

class testing:
    def complete(self,data):
        sentence = ''
        for get in data:
            if(type(get) is list):
                sentence += " "+str(get[0])
            else:
                sentence += " " + str(get)
        sentence_s = sentence.strip()
        return sentence_s

    def testing(self):
        # Give the location of the file
        loc = ("sentence100_test.xlsx")

        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)

        wb_s = openpyxl.Workbook()
        sheet_s = wb_s.active

        tran = Translate()
        start =1
        data_translated =[]
        cc = 0
        header=['ประโยคที่มีคำว่าของ','ประโยคคำถาม','ประโยคที่มีการบอกลักษณะนาม','ประโยคที่มีการใช้ โดย']
        for i in range(sheet.nrows-start):
            get_thai = sheet.cell_value(i+start, 1)
            sentence_thai =str(get_thai)
            # print(sentence_thai,"\n")

            if(sentence_thai not in header):
            # sentence_thai = 'บ้านของฉัน'
                cc+=1
                sentence_hmong = self.complete(tran.traslateThaiHmong(sentence_thai)[0])
            else:
                sentence_hmong =''
            data_translated.append((sentence_thai,sentence_hmong))
        print(data_translated)
        print("จำนวนประโยค :",cc)

        print("\n---------------------------------------------------------------\n")
        for get in data_translated:
            print(get[1])

    def translate(self,sentence):
        tran = Translate()
        sentence_hmong = self.complete(tran.traslateThaiHmong(sentence)[0])
        # print(sentence_hmong)
        return sentence_hmong

if __name__ == '__main__':

    a= testing()
    # a.testing()

    text ="""
ผมไม่ทราบคำจำกัดความของคำนี้


    """
    text = text.strip()
    text = text.splitlines()
    all = []
    for sentence in text:
        sentence = sentence.strip()
        all.append(a.translate(sentence))
    print("\n\n")
    for sentence in all:
        print(sentence)

