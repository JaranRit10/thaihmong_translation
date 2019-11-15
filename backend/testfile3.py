
if __name__ == '__main__':
    import tltk.nlp
    text = "เราเดินทางไปโรงเรียน"
    segment = tltk.nlp.word_segment(text).split('|')
    print("ผลลัพธ์ : ",segment)






