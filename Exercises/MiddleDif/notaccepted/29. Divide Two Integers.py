def divide(dividend, divisor):
    boolCheck= True
    addMinus = False
    answer = 0
    if dividend < 0 and divisor < 0:
        dividend = dividend * -1
        divisor = divisor * -1
    elif dividend < 0:
        dividend = dividend * -1
        addMinus = True
    elif divisor < 0:
        divisor = divisor * -1
        addMinus = True

    while boolCheck:
        if dividend-divisor >= 0:
            answer += 1
            dividend -= divisor
        else:
            break
    if addMinus:
        answer = answer * -1
    if answer > 2147483647:
        return 2147483647
    if answer < -2147483648:
        return -2147483648

    return answer

print(divide(-1210, 12)) #TIME LIMIT EXCEEDED!