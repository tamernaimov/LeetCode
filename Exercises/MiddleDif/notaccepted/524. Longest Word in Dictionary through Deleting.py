def findLongestWord(s,dictionary):
    longest = 0
    curWord = ""
    for i in range (len(dictionary)):
        counter = 0
        for c in dictionary[i]:
            if c in s:
                counter+=1
        if counter > longest:
            longest = counter
            curWord = dictionary[i]
    return curWord

print(findLongestWord("abce",["abe","abc"])) #something with the alphabetical order is not right