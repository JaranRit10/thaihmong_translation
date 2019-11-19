from jiwer import wer

"""
    wer = (การแทนที่ + การแทรก + การลบ)/ จำนวนประโยคอ้างอิง
"""

ground_truth = ["i an run"]
hypothesis = ["i tin run"]

wer = wer(ground_truth, hypothesis)
print("wer : ",wer)
print("WAcc : ",1-wer)