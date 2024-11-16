def longestValidParentheses(s):
    longestPar = 0
    i = 0
    counter = 0
    while i < len(s) - 1:
        text = s
        if text[i] + text[i + 1] == "()":
            text.replace(text[i],  "")
            text.replace(text[i+1],  "")
            print(i)
            counter += 2
            i += 2
        else:
            counter = 0
            i += 1
            continue
        if counter > longestPar:
            longestPar = counter

    return longestPar


print(longestValidParentheses("()(()()(()()"))
