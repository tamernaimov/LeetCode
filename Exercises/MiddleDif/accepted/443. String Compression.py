from itertools import count


def compress(chars):
    ans = 0
    i = 0

    while i < len(chars):
        letter = chars[i]
        counter = 0
        while i < len(chars) and chars[i] == letter:
            counter += 1
            i += 1
        chars[ans] = letter
        ans += 1
        if counter > 1:
            for c in str(counter):
                chars[ans] = c
                ans += 1

    return ans


print(compress(["a","a","b","b","c","c","c"]))