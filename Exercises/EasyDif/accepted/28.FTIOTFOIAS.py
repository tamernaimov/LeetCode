class Solution():
    def strStr(s,haystack, needle):  # haystack = the whole word needle = part
        for i in range(len(haystack)):
            if haystack[i:i + len(needle):] == needle:
                return i
        return -1


