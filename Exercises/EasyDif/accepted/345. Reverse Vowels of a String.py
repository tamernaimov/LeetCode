def reverseVowels(s):
    checker = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    l = 0
    r = len(s) - 1

    while l < r:

        if s[l] in checker and s[r] in checker:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        elif s[l] not in checker:
            l += 1
        elif s[r] not in checker:
            r -= 1


    return "".join(s)

result = reverseVowels("IceCream")
print(result)