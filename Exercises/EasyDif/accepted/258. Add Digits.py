def addDigits(num):
    while len(str(num)) != 1:
        sum = 0
        for i in range(len(str(num))):
            strNum = str(num)[i]
            sum += int(strNum)
        num = sum
    return num

print(addDigits(384))