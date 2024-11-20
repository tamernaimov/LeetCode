def isHappy(num):
    sum = 0
    counter = 0
    while sum != 1:
        sum = 0
        strNum = str(num)
        for i in range(len(strNum)):
            sum += (int(strNum[i]) * int(strNum[i]))
            num = sum
        counter += 1
        if counter > 1000:
            return False

    return True

print(isHappy(2))