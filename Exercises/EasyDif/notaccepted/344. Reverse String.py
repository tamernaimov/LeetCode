def reverseString(s):
    word = ""
    unique_word = ""
    for char in s:
        word += char

    for i in range(len(word) -1 ,-1,-1):
        print(word[i])
        unique_word += word[i]
    unique_list = []
    for i in range (len(unique_word)):
        unique_list.append(unique_word[i])

    s = unique_list[:]
    return s
print(reverseString(["h","e","l","l","o"]))