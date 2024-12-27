import itertools

def findSubstring(s,words):


    answers = []
    print(words)
    for i in range(len(words)):
        for j in range(len(s)-len(words)):
            if words[i] == s[j:len(words[i])+j]:
                answers.append(j) #problem here
                print("asd")

    answers = list(dict.fromkeys(answers))
    return answers

print(findSubstring("asdasdasd",["asd"]))