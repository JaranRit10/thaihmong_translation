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
        header=['ประโยคที่มีคำว่าของ','ประโยคคำถาม','ประโยคที่มีการบอกลักษณะนาม','ประโยคที่มีการใช้ โดย']
        for i in range(sheet.nrows-start):
            get_thai = sheet.cell_value(i+start, 1)
            sentence_thai =str(get_thai)
            # print(sentence_thai,"\n")

            if(sentence_thai not in header):
            # sentence_thai = 'บ้านของฉัน'
                sentence_hmong = self.complete(tran.traslateThaiHmong(sentence_thai)[0])
            else:
                sentence_hmong =''
            data_translated.append((sentence_thai,sentence_hmong))
        print(data_translated)


        print("\n---------------------------------------------------------------\n")
        for get in data_translated:
            print(get[1])



if __name__ == '__main__':
    a= testing()
    a.testing()