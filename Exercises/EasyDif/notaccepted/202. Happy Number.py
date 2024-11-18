def isHappy(num):
    strNum = str(num)
    sum = 0
    while sum != 1:
        for i in range(len(strNum)):
            print(len(strNum))
            sum = 0
            sum += int(strNum[i]) * int(strNum[i])
            strNum = str(sum)

    return True

print(isHappy(19))