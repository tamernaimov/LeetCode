def validPalindrome(s):
    if s[::1] == s[::-1]:
        return True

    for i in range(len(s)):
        tester = s[:i] + s[i+1:]
        print(tester)
        if tester[::1] == tester[::-1]:
            return True
    return False

print(validPalindrome("cbbcc"))