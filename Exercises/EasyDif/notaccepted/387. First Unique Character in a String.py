def firstUniqChar(s):
    boolCheck = False
    stringExample = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)-1):
            if s[i] == s[j]:
                boolCheck = True
                stringExample += s[i]
                break
        if boolCheck:
            return stringExample
print(firstUniqChar("asdasdas"))