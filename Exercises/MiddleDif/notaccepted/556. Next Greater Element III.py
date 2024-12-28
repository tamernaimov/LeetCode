

def nextGreaterElement(n):
    nStr = str(n)
    nStr = [char for char in nStr]
    r = len(nStr)-1
    l = len(nStr)-2
    print(nStr)
    while r != 0:
        if nStr[l] < nStr[r]:
            nStr[l],  nStr[r] = nStr[r], nStr[l]
            return nStr

        if l == 0:
            r-=1
            l = r-1

        l-=1




    return nStr


print(nextGreaterElement(5291))