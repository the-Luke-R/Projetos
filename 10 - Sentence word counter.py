sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
words = []
for i in sentences:
    words.append(i.count(" ") + 1)
print(max(words))