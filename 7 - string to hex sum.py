string = "Forty4Three"
numbers = []

for i in string:
    result = hex(ord(i))
    numbers = result[-2] + result[-1]
    for j in numbers:
        if j.isalpha():
            continue
        else:
            numbers.append(int(j))
print(sum(numbers))