import backend.Database
from backend.Grammar import Grammar
from backend.prob import prob
import json
import time,timeit
import multiprocessing as mp
import time
import ast

class Translate():

    # __|font , center_f|center_b , back|__ หลักการคิดการคำนวณ bigram
    def bigramprob(self,word):
        print("used method bigramprob")
        def sort(e):
            return e['prob']
        for i in range(0,len(word)):
            try:
                if (type(word[i]) is list and len(word[i]) > 1):
                    bigram = prob()
                    propWord = []
                    for j in range(0, len(word[i])):
                        try:
                            splitFont = word[i-1].split()
                            split_last = splitFont[len(splitFont)-1]
                            center_f =  word[i][j].split()
                            center_f = center_f[0]
                            # print("--",split_last,"*",center_f)
                            font = bigram.propbigram(split_last, center_f)
                            if (font[1] == 0):
                                font = (False, 0.0001)

                        except Exception as e:
                            print(e)
                            font = (False, 0.0001)
                        try:
                            splitBack = word[i+1].split()
                            split_first = splitBack[0]
                            center_b = word[i][j].split()
                            center_b = center_b[len(center_b)-1]

                            print(split_first)
                            back = bigram.propbigram(center_b, split_first)
                        except Exception as e:
                            print(e)
                            back = (False, 0.0001)
                        if (back[1] == 0):
                            back = (False, 0.0001)
                        # print(f"font {word[i-1],word[i][j]} :{font}")
                        # print(f"back {word[i][j],word[i+1]}:{back}")
                        update = {'word': word[i][j], 'prob': font[1] * back[1]}
                        propWord.append(update)
                    propWord.sort(reverse=True, key=sort)
                    print(propWord)
                    get = []
                    for w in propWord:
                        get.append(w.get('word'))
                    word.pop(i)
                    word.insert(i,get)
                    # print(word)
            except Exception as e:
                print(e, "in method bigramprob")

        return word

    # สำหรับการแปลภาษาไทย-ม้ง โดยเข้าประโยคเข้ามาใน method
    def traslateThaiHmong_0(self,allSentence):
        usegrammar = Grammar()
        data = backend.Database.Database()
        sendResult = " "
        try:
            allSentence = str(allSentence)
            getSentence = allSentence.split("\n")
            firstSentence = True
            for sentence in getSentence :
                # for one check word not have in the database
                check =True
                result = ""
                wordlist = usegrammar.grammarHmong(sentence)
                # loop check word in sentence
                for i in range(0, len(wordlist) - 1):
                    get = data.searchFortran(wordlist[i][0],wordlist[i][1])

                    result = result + get[0][2]+" "
                    # for insert sentence one time and first word
                    if(check==True and get[0][0]=='None'):
                        print(get)
                        # print("insert :"+str(get[0][1])+" "+get[0][3])
                        # print('sentence :'+sentence)
                        # insert to database
                        check=False
                    # for insert sentence that more two word
                    elif(get[0][0]=='None'):
                        pass

                if (firstSentence==True):
                    sendResult = result
                    firstSentence = False
                else:
                    sendResult = sendResult + "|\\" + result
            return sendResult

        except Exception as e:
            print(e)
            print("in method traslateThaiHmong_0")
            return sendResult


    continue_word =["ๆ"]
    buffer_sentence = {}
    def traslateThaiHmong(self,allSentence):
        usegrammar = Grammar()
        # getPlob = Translate()
        data = backend.Database.Database()
        # for clear buffer
        if (len(self.buffer_sentence)>500):
            self.buffer_sentence.clear()
        try:
            allSentence = str(allSentence)
            getSentence = allSentence.split("\n")

            s_sentence =[]
            for  sentence in getSentence :
                sentence = sentence.strip()
                if sentence is None:
                    print("sentence is null")
                    continue
                # for buffer sentence made the program not try again.
                if(sentence  not in self.buffer_sentence):
                    wordlist = usegrammar.grammarHmong(sentence)
                    # print("wordlist :"+str(wordlist))
                    # loop check word in sentence
                    s_word = []
                    newword =[]
                    for i in range(0, len(wordlist) - 1):
                        # print(wordlist[i][0],wordlist[i][1])
                        if(wordlist[i][0] in self.continue_word):
                            continue
                        if(wordlist[i][1]=="NUM"):
                            try:
                                # สำหรับแปลตัวเลข
                                number = int(wordlist[i][0])
                                number = number+1
                                get = [(0, wordlist[i][0], wordlist[i][0], 'NUM', 0, 0)]
                            except:
                                print("sentence have a number.")
                                get = data.searchFortran(wordlist[i][0], wordlist[i][1])
                        else:
                            get = data.searchFortran(wordlist[i][0],wordlist[i][1])
                        # print(len(get))
                        # print(get)
                        if(len(get)>1):
                            w =[]
                            for gett in get:
                                w.append(gett[2])
                            s_word.append(w)
                        else:
                            # print(get[0][2])
                            g = get[0][2]
                            s_word.append(str(g))
                            try:
                                if (get[0][0] == "None"):
                                    newword.append(get[0])


                            except Exception as e:
                                print(e)
                                # print("Error in sub method traslateThaiHmong")

                    # s_word = getPlob.bigramprob(s_word)
                    s_word = self.bigramprob(s_word)
                    self.buffer_sentence[sentence] = s_word
                else:
                    print("get in buffer")
                    s_word = self.buffer_sentence[sentence]
                print("s_word : ",s_word)
                s_sentence.append(s_word)
                # print(newword)

                # for add newword to database
                # if(newword !=[]):
                #     print(sentence)
                #     hmong_sentence =""
                #     for word in s_word:
                #         hmong_sentence+= word+" "
                #     hmong_sentence=hmong_sentence.strip()
                #     print(hmong_sentence)
                #     id_sentence  = data.insertSentence_newword(sentence,hmong_sentence)
                #     for newword in newword:
                #         data.insertNewword_toNewword(id_sentence,newword[1],newword[3])

            return s_sentence

        except Exception as e:
            print(e)
            print("in method traslateThaiHmong")
            return s_sentence


    def traslateThaiHmong_Thread(self,allSentence):
        usegrammar = Grammar()
        # getPlob = Translate()
        data = backend.Database.Database()
        pool = mp.Pool(processes=5)
        try:
            allSentence = str(allSentence)
            getSentence = allSentence.split("\n")

            s_sentence =[]
            wordlist = []

            # for sentence in getSentence :
            #     wordlist.append(usegrammar.grammarHmong(sentence))
            # print(wordlist)

            pool = mp.Pool(processes=3)
            wordlist = (pool.map(usegrammar.grammarHmong, getSentence))
            print(wordlist)

            return wordlist

        except Exception as e:
            print(e)
            print("in method traslateThaiHmong")
            return s_sentence


if __name__ == '__main__' :

    ss = time.time()
    tt = Translate()
    while(1):
        ww = input("input :")
        aa = tt.traslateThaiHmong(ww)
        print(aa)
    print(time.time()- ss)
    # i=0
    # use = []
    # sen = ["ไปด้วยกัน","กินข้าวกันยัง","เราเพื่อนกัน"]
    # for i in range(0, len(sen)):
    #     for i in range(0,len(sen)):
    #         t = sen[i]
    #         s = time.time()
    #         ss = tt.traslateThaiHmong(t)
    #         print(ss)
    #         ts = time.time()
    #         print("time :",ts-s)
    #         use.append(ts-s)
    # print(use)
    # print("เวลาเฉลี่ย :",(sum(use)/len(use)))
    #
    #


