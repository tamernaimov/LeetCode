class Solution(object):
    def myPow(self, x, n):
        answer = 1
        if n > 0:
            for i in range(n):
                answer = answer * x
            return answer
        elif n < 0:
            n = -n
            for i in range(n):
                answer = answer * x
            return 1 / answer

    def myPow2(self,x, n):  # works too lmao
        return x ** n
