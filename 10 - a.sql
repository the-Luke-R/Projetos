item = [174]

if not item:
    print("[]")
else:
    for i in item:
        if i == min(item):
            item.remove(i)
            print(item)
            break