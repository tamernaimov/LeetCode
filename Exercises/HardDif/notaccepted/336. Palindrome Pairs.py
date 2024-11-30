def palindromePairs(words):
    unique_list = []
    for i in range(len(words)-1):
        print(i)
        if words[i] + words[i+1] == (words[i]+words[i+1])[::-1]:
            unique_list.append([i,i+1])
        if words[i+1] + words[i] == (words[i+1]+words[i])[::-1]:
            unique_list.append([i+1,i])

    return unique_list


print(palindromePairs(["abcd","dcba","lls","s","sssll"]))


def palindromePairs2(words):
    unique_list = []
    for i in range(len(words)):
        if words[i][::-1] in words:
            unique_list.append([i,i+1])