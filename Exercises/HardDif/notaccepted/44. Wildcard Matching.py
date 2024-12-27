def isMatch(s,p): #aa,?b
    boolCheck = True
    if len(p) > len(s):
        return False

    if len(p) == 1:
        if p[0] == "*":
            return True
    if len(s) > len(p) and "*" not in p:
        return False

    for i in range(len(s)):
        if p[i] == "?":
            temp = p.replace(p[i], s[i])
            p = temp

    for i in range(len(s)):
        indexes = []
        if p[i] == "*":
            indexes.append(i)

            temp = p.replace(p[i],s[i:len(s)-1])
    return True

print(isMatch("abfff","a*f?"))