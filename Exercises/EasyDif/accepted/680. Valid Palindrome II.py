def validPalindrome( s):
        if s == s[::-1]:
            return True

        s = list(s)
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                skip_left = s[l+1:r+1] == s[l+1:r+1][::-1]
                skip_right = s[l:r] == s[l:r][::-1]

                if skip_left or skip_right:
                    return True
                else:
                    return False

            l += 1
            r -= 1

        return True

print(validPalindrome("deeee"))