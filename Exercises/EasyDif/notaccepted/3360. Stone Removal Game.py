def canAliceWin(n):
    remover = 10
    i = 0
    while n>=0:
        n-=remover
        i+=1
        remover -=1
    if i == 0 or i %2 == 0:
        return True
    return False

print(canAliceWin(49))