def isValid(s):
    i = 0
    while i < len(s)-1:
        if s[i] + s[i+1] == "()" or s[i] + s[i+1] == "[]" or s[i] + s[i+1] == "{}":
            s.replace(s[i+1],"")
            s.replace(s[i],"")
            i = 0
            print(s)
        else:
            i += 1

    print(s)

print(isValid("()"))