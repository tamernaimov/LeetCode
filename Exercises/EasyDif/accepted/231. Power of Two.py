

def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


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
print(isPowerOfTwo(8))