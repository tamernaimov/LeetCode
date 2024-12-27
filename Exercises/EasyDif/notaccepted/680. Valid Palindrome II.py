from traceback import print_tb


def validPalindrome(s):
    if s[::1] == s[::-1]:
        return True

    i = 0
    j = len(s)-1
    while i != j:

        if s[i] == s[j]:
            continue
        else:
            s = s.replace(s[i], "")
    if s[::1] == s[::-1]:
            return True
    else:
        return False


print(validPalindrome("caba"))