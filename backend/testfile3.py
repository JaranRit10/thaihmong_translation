

if __name__ == '__main__':
    classifier_word = ['สัก']
    senten_list = [('เขา', 'PRON'), ('ต้องการ', 'VERB'), ('เช่าบ้าน', 'NOUN'), ('สัก', 'ADV'), ('หลัง', 'NOUN'), ('<s/>', 'PUNCT')]
    if(classifier_word in da for da in senten_list):
        print("OK")