

if __name__ == '__main__':
    questionword = ['หรือเปล่า', 'หรือยัง', 'เปล่า', 'ไหม']
    senten_list = [('ขอ', 'VERB'), ('ฉัน', 'PRON'), ('ลอง', 'VERB'), ('ได้', 'ADV'), ('ไหม', 'PART'), ('<s/>', 'PUNCT')]
    print(senten_list[len(senten_list) - 2][0] in questionword)
    if (senten_list[len(senten_list) - 2][0] in questionword and
            senten_list[len(senten_list) - 3][0] == "ได้"):
        print("------------OK--------------------")