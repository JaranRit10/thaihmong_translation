

class f_measure:
    def dff(self,sentence_correct,thai_hmong,google,microsoft):

        sentence_correct = sentence_correct.split()
        thai_hmong = thai_hmong.split()
        google = google.split()
        microsoft = microsoft.split()

        total = []
        total.append(thai_hmong)
        total.append(google)
        total.append(microsoft)
        print(total)
        correct = []
        for sentence in total:
            true = 0
            sentence_true = []
            for word in sentence:
                if (word in sentence_correct):
                    true += 1
                    sentence_true.append(word)
            correct.append([true, sentence_true])

        print(correct)
        system = ["myprojec", "google", "microsoft"]
        output = []
        for i in range(len(correct)):
            pre = correct[i][0] / len(total[i])
            re = correct[i][0] / len(sentence_correct)
            get = {
                "precision": correct[i][0] / len(total[i]),
                "recall": correct[i][0] / len(sentence_correct),
                "f_measure": 2 * ((re * pre) / (re + pre))
            }
            output.append(get)

        print("\n--------------------\n")

        for i in output:
            print(i)
        return output

if __name__ == '__main__':
    sentence_correct = 'thov  Kuv qhia Kuv tus npawg rau Koj me ntsis '

    thai_hmong = 'thov  Kuv qhia Kuv tus npawg rau Koj me ntsis '
    google = 'Kuv tuaj yeem qhia kuv cov phooj ywg rau koj'
    microsoft = 'Cia kuv ua kom paub kuv cov phooj ywg rau koj'

    a = f_measure()
    tt= a.dff(sentence_correct,thai_hmong,google,microsoft)
    print("tt :",tt)