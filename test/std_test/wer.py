from jiwer import wer

ground_truth = ["hello world", "i like python"]
hypothesis = ["hello duck", "i like python"]

error = wer(ground_truth, hypothesis)
print(error)


ground_truth = ["hello world"]
hypothesis = ["hello duck"]

error = wer(ground_truth, hypothesis)
print(error)