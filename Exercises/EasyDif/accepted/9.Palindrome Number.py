class Solution():
    def isPalindrome(self,x):
        x = str(x)
        y = x[::-1]
        if x == y:
            return True
        else:
            return False
