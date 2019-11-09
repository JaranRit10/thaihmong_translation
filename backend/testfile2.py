
import  tltk.nlp

Text = 'ผมสบายดี ขอบคุณ แล้วคุณล่ะ'

Text = Text.strip()

commar = Text.find(" ")
if (commar != -1):
    Text = Text.split()
    Text = ",".join(Text)
tltk.nlp.pos_tag(Text)
WordLst = tltk.nlp.word_segment(Text).split('|')
# print("แบบ 2 : " + str(tltk.nlp.pos_tag_wordlist(WordLst)))
senten_list = tltk.nlp.pos_tag_wordlist(WordLst)

# print(list)
# print(type(list))

print("ผลลัพธ์เริ่มต้น : " + str(senten_list))
