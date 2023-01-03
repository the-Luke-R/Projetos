# returns the sentence with most words

sentences = ["Man of Few Words", "semper fi", "Right Out of the Gate"]
words = []
for i in sentences:
    words.append(i.count(" ") + 1)
print(max(words))