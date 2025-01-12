import itertools

def findSubstring(s, words):
    permutations = itertools.permutations(words)
    combined_words = [''.join(p) for p in permutations]
    words = list(set(combined_words))

    print(words)
    answers = []
    for i in range(len(s)):
        for j in range (len(words)):
            if words[j] == s[i:i+len(words[j])]:
                answers.append(i)
    return answers

print(findSubstring("foobarfoobar",["foo","bar"]))