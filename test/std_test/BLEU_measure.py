
from nltk.translate.bleu_score import sentence_bleu
reference = [['kuv', 'lub', 'tsev','no'],['kuv', 'li', 'tsev']]

thai_hmong = 'thov  Kuv qhia Kuv tus npawg rau Koj me ntsis '
google = 'Kuv tuaj yeem qhia kuv cov phooj ywg rau koj'
microsoft = 'Cia kuv ua kom paub kuv cov phooj ywg rau koj'

candidate = ['kuv', 'li', 'tsev']


print('Cumulative 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
print('Cumulative 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))
print('Cumulative 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))
print('Cumulative 4-gram: %f' % sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))



#
# from nltk.translate.bleu_score import sentence_bleu
# text = 'thov  Kuv qhia Kuv tus npawg rau Koj me ntsis '
# text = text.split()
#
# reference = text
#
# thai_hmong = 'thov  Kuv qhia Kuv tus npawg rau Koj me ntsis '
# google = 'Kuv tuaj yeem qhia kuv cov phooj ywg rau koj'
# microsoft = 'Cia kuv ua kom paub kuv cov phooj ywg rau koj'
#
# thai_hmong = thai_hmong.split()
# google = google.split()
# microsoft = microsoft.split()
#
# candidate = []
# candidate.append(thai_hmong)
# candidate.append(google)
# candidate.append(microsoft)
#
# output =[]
# print(candidate)
# for sentence in candidate:
#     # print('Cumulative 1-gram: %f' % sentence_bleu(reference, sentence, weights=(1, 0, 0, 0)))
#     # print('Cumulative 2-gram: %f' % sentence_bleu(reference, sentence, weights=(0.5, 0.5, 0, 0)))
#     # print('Cumulative 3-gram: %f' % sentence_bleu(reference, sentence, weights=(0.33, 0.33, 0.33, 0)))
#     # print('Cumulative 4-gram: %f' % sentence_bleu(reference, sentence, weights=(0.25, 0.25, 0.25, 0.25)))
#     uni = sentence_bleu(reference, sentence, weights=(1, 0, 0, 0))
#     bi = sentence_bleu(reference, sentence, weights=(0.5, 0.5, 0, 0))
#     tri = sentence_bleu(reference, sentence, weights=(0.33, 0.33, 0.33, 0))
#     four = sentence_bleu(reference, sentence, weights=(0.25, 0.25, 0.25, 0.25))
#     output.append((uni,bi,tri,four))
# print(output)


