




reference = """
The cat is on the mat
There is a cat on the mat
"""

candidate ="""
the cat the cat on the mat
"""

# Thov pab qhia sau lub npe
# Koj yuav tau pab tsiaj koj lub npe

reference = reference.strip().split("\n")
candidate = candidate.strip().split("\n")
t = []
for i in reference:
    t.append(i.split())
for j in candidate

reference = [reference.split()]
candidate = candidate.split()
print(reference,'\n',candidate)
from nltk.translate.bleu_score import sentence_bleu
# reference = [['the',  'brown', 'fox', 'jumped', 'over', 'the']]
# candidate = ['the',  'brown', 'fox', 'jumped', 'over', 'the']
score = sentence_bleu(reference, candidate)
print(score)