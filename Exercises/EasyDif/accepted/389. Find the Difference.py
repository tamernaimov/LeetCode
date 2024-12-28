def findTheDifference(s,t):
    if len(s) == 0:
        return t[0]

    for i in range(len(s)):
       if s[i] in t:
           t = t.replace(s[i],"")

    return t
print(findTheDifference("","b"))