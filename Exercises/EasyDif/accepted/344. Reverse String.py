def reverseString(s):
    another_list = []
    for i in range(len(s)-1,-1,-1):
        another_list.append(s[i])

    for i in range(len(s)):
        s[i] = another_list[i]
    return s
print(reverseString(["h","e","l","l","o"]))