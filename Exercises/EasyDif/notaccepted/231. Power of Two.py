

def isPowerOfTwo(n):
    if n == 1:
        return True
    for i in range (n):
        if i*i == n:
            return True
    return False


def isPowerOfTwo2(n):
    left = 0
    right = n
    while left<= right:
        middle = (left+right)//2
        if middle*middle > n:
            right = middle-1
        elif middle*middle < n:
            left = middle+1
        else:
            return True
    return False
print(isPowerOfTwo2(8))