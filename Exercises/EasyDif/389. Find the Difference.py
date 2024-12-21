

def findTheDifference(s,t):
    test = t
    for i in range(len(s)):
        if t[i] == s[i]:
            test = test.replace(t[i],"",1)

    return test
print(findTheDifference("a","aa"))