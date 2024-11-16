def isPerfectSquare(num:int):
    left = 0
    right = num

    while left <= right:
        middle = (left+right)//2
        if middle*middle > num:
            right = middle-1
        elif middle*middle < num:
            left = middle+1

        if middle*middle == num:
            return True
    return False

print(isPerfectSquare(7))
print()