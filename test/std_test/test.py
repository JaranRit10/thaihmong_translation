


from nltk.translate.bleu_score import sentence_bleu

re = 'pev paus tau sib ntsib dua'
re = re.lower()
re = re.split()

can = 'peb puas tau ntsib ua ke los ua ntej'
can = can.lower()
can = can.split()
print(re,can)
reference = [re]
candidate = can
score = sentence_bleu(reference, candidate)
print(score)