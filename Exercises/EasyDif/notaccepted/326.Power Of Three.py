def isPowerOfThree(n):
    left = 0
    right = n
    if n == 0:
        return False
    while left <= right:
        mid = (left+right)//2

        if mid * mid * mid > n:
            right = mid - 1
        elif mid * mid * mid < n:
            left = mid +1
        else:
            return True
    return False
print(isPowerOfThree(6))