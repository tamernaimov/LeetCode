def isSubsequence(s,t):
    indexes = []
    for i in range (len(s)):
        checker = False
        for j in range(len(t)-1,-1,-1):
            if s[i] == t[j]:
                checker = True
                indexes.append(j)
                t = t.replace(t[j],"")
                break
        if not checker:
            return False

    indexes2 = indexes[:]
    indexes2.sort()
    print(indexes)

    if indexes == indexes2:
        return True
    return False


print(isSubsequence("ab","baab"))

