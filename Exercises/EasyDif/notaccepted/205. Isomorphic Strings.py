def isIsomorphic(s,t):
    list1 = []
    list2 = []
    for i in range (len(s)):
        if s[i] not in list1:
            list1.append(s[i])

    for i in range (len(t)):
        if t[i] not in list2:
            list2.append(t[i])


    if len(list1) == len(list2):
        return True
    return False

print(isIsomorphic("egg","add"))