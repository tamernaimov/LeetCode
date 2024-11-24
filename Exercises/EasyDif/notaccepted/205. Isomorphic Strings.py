def isIsomorphic(s,t):
    for i in range(len(s)):
        s = s.replace(s[i],t[i])
        print(s)
    if s ==t:
        return True
    else:
        return False

isIsomorphic("badc","baba")