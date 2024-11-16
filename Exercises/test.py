

def longestPalindrome(s):
    longest = ""
    longestInside = ""
    for i in range(len(s)):  # 5
        for j in range(len(s) - 1, i, -1):
            if s[i] == s[j]:  # i = 1 j = 2
                print(j)
                print(i)
                longestInside = s[j:i - 1:-1]

        if len(longestInside) > len(longest):
            longest = longestInside

    if longest == "":
        return s[0]
    return longest

print(longestPalindrome("tanatra"))

word = "Tamer"
print(word[3:2:-1])