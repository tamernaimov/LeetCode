def findNthDigit(n):
    stringN = ""

    for i in range(1,n+1):
        stringN += str(i)

    return int(stringN[n-1])
print(findNthDigit(100000000))