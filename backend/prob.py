import re
import ast
import os

class prob:
    def readFile(self,fileName):
        data = []
        file = open(fileName, "r")
        dataset = file.read()
        dataset = dataset.lower()
        dataset = re.split('\n', dataset)
        for get_sentence in dataset:
            sentence = get_sentence.strip()
            if(sentence !=''):
                get = re.findall(r"[\w']+", sentence)
                # print((get))
                get.insert(0,"<s>")
                get.insert(len(get),"</s>")
                # print(get)
                data.append(get)

        return data

    def createBigram(self,data):
        listOfBigrams = []
        bigramCounts = {}
        unigramCounts = {}
        nbyn = {}
        for data in data:
            for i in range(len(data)):
                if i < len(data) - 1:
                    listOfBigrams.append((data[i], data[i + 1]))
                    if (data[i], data[i + 1]) in bigramCounts:
                        bigramCounts[(data[i], data[i + 1])] += 1
                    else:
                        bigramCounts[(data[i], data[i + 1])] = 1

                if data[i] in unigramCounts:
                    unigramCounts[data[i]] += 1
                else:
                    unigramCounts[data[i]] = 1
        return listOfBigrams, unigramCounts, bigramCounts

    def createTrigram(self, data):
        listOfBigrams = []
        bigramCounts = {}
        unigramCounts = {}
        nbyn = {}
        for data in data:
            for i in range(len(data)):
                if i < len(data) - 1:
                    listOfBigrams.append((data[i], data[i + 1]))
                    if (data[i], data[i + 1]) in bigramCounts:
                        bigramCounts[(data[i], data[i + 1])] += 1
                    else:
                        bigramCounts[(data[i], data[i + 1])] = 1
                if data[i] in unigramCounts:
                    unigramCounts[data[i]] += 1
                else:
                    unigramCounts[data[i]] = 1
        # print(listOfBigrams)
        return listOfBigrams, unigramCounts, bigramCounts

    def calcBigramProb(self,listOfBigrams, unigramCounts, bigramCounts):

        listOfProb = {}
        for bigram in listOfBigrams:
            word1 = bigram[0]
            word2 = bigram[1]

            listOfProb[bigram] = (bigramCounts.get(bigram)) / (unigramCounts.get(word1))

        return listOfProb

    def addOneSmothing(self,listOfBigrams, unigramCounts, bigramCounts):
        listOfProb = {}
        cStar = {}
        for bigram in listOfBigrams:
            word1 = bigram[0]
            word2 = bigram[1]
            listOfProb[bigram] = (bigramCounts.get(bigram) + 1)/(unigramCounts.get(word1) + len(unigramCounts))
            cStar[bigram] = (bigramCounts[bigram] + 1) * unigramCounts[word1] / (unigramCounts[word1] + len(unigramCounts))
        return listOfProb, cStar

    def start(self):
        fileName = 'file/Dataset.txt'
        data = self.readFile(fileName)
        listOfBigrams, unigramCounts, bigramCounts = self.createBigram(data)
        # print(listOfBigrams)
        # print(unigramCounts)
        # print(bigramCounts)
        prob = self.calcBigramProb(listOfBigrams, unigramCounts, bigramCounts)
        f = open("file/bigramProb.txt", "w")
        f.write(str(prob))
        f.close()
        return prob

        return  prob

    def start_add(self):
        fileName = 'file/Dataset.txt'
        data = self.readFile(fileName)
        listOfBigrams, unigramCounts, bigramCounts = self.createBigram(data)
        # print(listOfBigrams)
        # print(unigramCounts)
        # print(bigramCounts)
        prob = self.addOneSmothing(listOfBigrams, unigramCounts, bigramCounts)
        f = open("file/addOneSmoothing.txt", "w")
        f.write(str(prob[0]))
        f.close()
        return  prob[0]

    def propbigram(self,w1,w2):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'file/bigramProb.txt')
        # filename = os.path.join(dirname, 'file/addOneSmoothing.txt')
        f = open(filename, "r")
        prob = f.read()
        prob = ast.literal_eval(prob)
        f.close()
        w1 = str(w1)
        w2 = str(w2)
        w1 = w1.lower()
        w2 = w2.lower()
        bigram = (w1, w2)

        # print(bigram in prob)
        # print(prob[bigram])

        try:
            return ((bigram in prob),prob[bigram])
        except Exception as e:
            print("word have not!! ",e)
            return False,0


if __name__ == '__main__':

    b = prob()
    aa = b.start_add()
    print(b.propbigram("lub",'tsev'))
    print(0.00001*0.4)
    # b = prob()
    # aa = b.start()
    # print("aa :",aa)
    # for a,b in aa.items():
    #     print(a,b)


