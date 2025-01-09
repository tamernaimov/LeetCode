import itertools
def checkInclusion(s1,s2):
    li = [''.join(p) for p in itertools.permutations(s1)]
    print(li)
    for i in range (len(li)):
        if li[i] in s2:
            return True

    return False


print(checkInclusion("ab","eidbaooo"))