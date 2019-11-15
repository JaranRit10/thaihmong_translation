# from microsofttranslator import Translator
# translator = Translator('<Your Client ID>', '<Your Client Secret>')
# print (translator.translate("Hello", "pt"))

tex = '''


'''
tex = tex.splitlines()
print(tex, "\n-------------------------------\n")
for i in tex:
    if (i != ''):
        print(i)


print("\n----------------------------------\n")

text2 ="""


"""
# text2 = text2.strip()
# text2 = text2.splitlines()
# for i in text2:
#     print(i,"\n")







# import openpyxl
# import xlrd
# from backend.Translate import Translate
#
# loc = ("sentence100_test.xlsx")
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
# sheet.cell_value(0, 0)
# wb_s = openpyxl.Workbook()
# sheet_s = wb_s.active
# tran = Translate()
# start = 1
# data_translated = []
# header = ['ประโยคที่มีคำว่าของ', 'ประโยคคำถาม', 'ประโยคที่มีการบอกลักษณะนาม', 'ประโยคที่มีการใช้ โดย']
# for i in range(sheet.nrows - start):
#     get_thai = sheet.cell_value(i + start, 1)
#     sentence_thai = str(get_thai)
#     print(sentence_thai, "\n")
