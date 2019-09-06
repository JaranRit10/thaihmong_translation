import ast
import time

w1 = "เราทำงาน"
w2 = "peb ua hauj lwm"
f = open("file/translate_sentence.txt", "r",encoding='utf-8')

ss = time.time()
prob = f.read()
prob = ast.literal_eval(prob)
w1 = str(w1)
w2 = str(w2)
w1 = w1.lower()
w2 = w2.lower()
bigram = (w1, w2)

f.close()

print(bigram in prob, prob[bigram])
print(time.time()-ss)