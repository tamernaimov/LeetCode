def validPalindrome(s):
    l = 0
    r = len(s)-1
    while l<=r:
        if s[l] != s[r]:
            s1 = s[l+1:r+1]
            s2 = s1[::-1]
            s3 = s[r-1:l:-1]
            temp = s[l]
            sComp = temp+s3
            s4 = s3[::-1]
            if s2 != s1 and sComp != s4:
                return False
        l+=1
        r-=1
    return True

print(validPalindrome("abca"))