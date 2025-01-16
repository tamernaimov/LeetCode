def reverseStr(s,k):

    firstStr = s[:k]
    reversedStr = firstStr[::-1]
    secStr = s[k:]
    return reversedStr+secStr


print(reverseStr("abcdefg",2))