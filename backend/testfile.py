import tltk.nlp
import deepcut
Text = "เรียนหนังสือปลาทอง"
tltk.nlp.pos_tag(Text)
WordLst = tltk.nlp.chunk(Text).split('|')
# print("แบบ 2 : " + str(tltk.nlp.pos_tag_wordlist(WordLst)))
list = tltk.nlp.pos_tag_wordlist(WordLst)
print(list)

a = deepcut.tokenize(Text)
print(a)