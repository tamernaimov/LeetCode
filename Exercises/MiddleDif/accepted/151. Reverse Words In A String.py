def reverseWords(s):
    s = s.strip()
    words = s.split(" ")
    unique_words = []
    newstr = ""
    for i in range (len(words)-1,-1,-1):
        if words[i] != "":
            unique_words.append(words[i])

    for i in range (len(unique_words)):
        newstr += unique_words[i]
        newstr += " "
    newstr = newstr.strip()

    return newstr