def reverseWords(s):
    s = s.split(" ")
    for i in range (len(s)):
        s[i] = s[i][::-1]
    return ' '.join(s)


print(reverseWords("Let's take LeetCode contest"))