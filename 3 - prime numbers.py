# returns the prime numbers of the number 600851475143

z = 600851475143

for x in range(2, 10000000):
    flag = 0
    if (z != 1):
        for y in range(2, x):
            if x % y == 0:
                flag = 1
                break
        if (flag != 1):
            while z % x == 0:
                z = z / x
                print(x)
    