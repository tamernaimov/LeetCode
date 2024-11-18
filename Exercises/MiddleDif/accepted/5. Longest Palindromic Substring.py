class Solution():
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            for j in range(len(s) - 1, i, -1):
                if s[i] == s[j]:
                    forward = s[i:j + 1]
                    reverse = s[j:i - 1:-1] if i > 0 else s[j::-1]
                    if forward == reverse:
                        if len(forward) > len(longest):
                            longest = forward

        return longest if longest else s[0]

print(Solution.longestPalindrome(Solution,"abfaa"))
