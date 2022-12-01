z = 600851475143

for x in range(2,10000000):
    flag=0
    if(z!=1):
        #print("x= " + str(x))
        for y in range(2,x):
            #print("y= " + str(y))
            if x % y == 0:
                #print("a")
                flag=1
                break
        #print("abc")
        if(flag!=1):
            while z % x == 0:
                z = z / x
                print(x)