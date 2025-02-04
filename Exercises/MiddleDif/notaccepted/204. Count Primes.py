def countPrimes(n):

    counter = 0

    for i in range (n):
        for j in range (2,i):
            if i % j == 0:
                counter+=1
                break

    return counter
print(countPrimes(10))