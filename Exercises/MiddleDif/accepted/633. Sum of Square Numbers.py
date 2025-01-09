import math
def judgeSquareSum(c):
        l = 1
        r = int(math.sqrt(c))
        print(r)
        while l<=r:
            if l*l + r*r > c:
                r-=1
            elif l*l + r*r < c:
                l+=1
            else:
                return True
        return False

print(judgeSquareSum(11))