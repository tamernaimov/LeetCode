def findAnagrams(s,p):
    results = []
    for i in range(len(s)):
        if sorted(p) == sorted(s[i:len(p)+i]):
            results.append(i)

    return results

print(findAnagrams("a","f"))