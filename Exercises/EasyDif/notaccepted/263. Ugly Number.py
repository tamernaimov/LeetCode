def isUgly(n):
    for i in range(1,n):
        if n%i == 0 and i != 2 and i != 3 and i != 5 and i!=1:
            return False
    return True

print(isUgly(26524654))