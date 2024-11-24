def countPrimes(n):
    counter = 0
    for i in range(n+1):
        if i ==2:
            counter +=1
            continue
        if i ==3:
            counter +=1
            continue
        if i == 1:
            continue
        if i % 2 !=0 and i % 3 !=0:
            print(i)
            counter+=1

    return counter

print(countPrimes(10))