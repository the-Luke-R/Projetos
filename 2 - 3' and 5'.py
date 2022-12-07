# Encontra todos os multiplos de 5 e 3 no range que colocarmos
# Returns the multiples of 3 and 5 in a determined range

x = 0
y = 0

for x in range(1000):
    if x % 5 == 0 or x % 3 == 0:
        y += x

print(y)
