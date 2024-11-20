def isPalindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    print(s)
    if s[::1] == s[::-1]:
        return True
    else:
        return False

print(isPalindrome("0P"))

