def countGoodSubstrings(s):

    s = list(s)
    print(s)
    res = 0
    seen = set()
    for i in range (len(s)-2):
        seen.clear()
        check = False

        for j in range (i,i+3):
            if s[j] not in seen:
                seen.add(s[j])
            else:
                check = True
                print(seen)
                break
        if not check:
            res +=1
    return res

print(countGoodSubstrings("aababcabc"))