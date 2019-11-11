if __name__ == '__main__':
    senten_list = [ ('นว', 'NOUN'), ('ดเท้า', 'NOUN'),('ผม', 'PRON'), ('ต้องการ', 'VERB'), ('<s/>', 'PUNCT')]
    Error = [('ดเท้า', 'นวดเท้า')]
    for word in senten_list:
        check = False
        for er in Error:
            if (er[0] in word):
                print("OK")
                index = senten_list.index(word)
                print(index)
                senten_list.pop(index)
                senten_list.pop(index-1)
                print(senten_list)
                senten_list.insert(index-1,(er[1],'NOUN'))
                print(senten_list)