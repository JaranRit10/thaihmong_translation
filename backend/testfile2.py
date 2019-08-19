from nltk import ngrams
import datetime

class check :


    sentence = """
        qhov khoom no yog leej twg li
        khoom ntawm no yog leej twg li
        ntse  kuv li
         
        """

    n = 2
    sixgrams = ngrams(sentence.split(), n)

    def bi_gram(self,first,next_word):
        count = 0
        num = 0
        for grams in self.sixgrams:
            # print(grams)
            if (grams[0] == first and grams[1] == next_word):
                count = count + 1
            num = num + 1
        return count/num


if __name__ == '__main__':
    cc = check()
    while(1):

        first = input("first :")
        next_word = input("next_word :")
        a = datetime.datetime.now()
        aa = cc.bi_gram(first, next_word)
        print(aa)
        z = datetime.datetime.now()
        print("time -->"+str(z-a))
