import re

class prop:
    def readFile(self,fileName):
        data = []
        file = open(fileName, "r")
        dataset = file.read()
        dataset = re.split('\n', dataset)
        for sentence in dataset:
            get = re.findall(r"[\w']+", sentence)
            # print((get))
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

    def calcBigramProb(self,listOfBigrams, unigramCounts, bigramCounts):

        listOfProb = {}
        for bigram in listOfBigrams:
            word1 = bigram[0]
            word2 = bigram[1]

            listOfProb[bigram] = (bigramCounts.get(bigram)) / (unigramCounts.get(word1))

        # file = open('bigramProb.txt', 'w')
        # file.write('Bigram' + '\t\t\t' + 'Count' + '\t' + 'Probability' + '\n')
        #
        # for bigrams in listOfBigrams:
        #     file.write(str(bigrams) + ' : ' + str(bigramCounts[bigrams])
        #                + ' : ' + str(listOfProb[bigrams]) + '\n')
        # file.close()
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
        fileName = '../Dataset.txt'
        data = self.readFile(fileName)
        listOfBigrams, unigramCounts, bigramCounts = self.createBigram(data)
        # print(listOfBigrams)
        # print(unigramCounts)
        # print(bigramCounts)

        prob = self.calcBigramProb(listOfBigrams, unigramCounts, bigramCounts)
        print(prob)
        prob = self.addOneSmothing(listOfBigrams, unigramCounts, bigramCounts)
        print(prob[0])
        return  prob

if __name__ == '__main__':
    a = prop()
    a = a.start()
    print(a)
