import codecs
import json
import ast
path = 'G:/thaihmong_translation/backend/file/addOneSmoothing.txt'

with open(path, 'r',) as file:
    data = file.read()
    # print(data)
    prob = ast.literal_eval(data)
    # print(type(prob))
    for key ,i in prob.items():
        print(key ,i)