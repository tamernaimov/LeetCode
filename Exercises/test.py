from random import Random


def canConstruct( ransomNote, magazine):
    for char1 in ransomNote:
        trueOrNot = False
        for char2 in magazine:
            if char1 == char2:
                trueOrNot = True
                magazine.replace(char2,"")
                break

        if not trueOrNot:
            return False
    return True
print(canConstruct("aa","ab"))
