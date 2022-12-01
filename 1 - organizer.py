# organiza uma lista de números em ordem crescente

a = [3,1,2,10,1]
b = []

for posicao in range(len(a)):
    if posicao == 0:
        b.append(a[posicao])
    else:
        b.append(a[posicao]+b[posicao-1])

print(b)