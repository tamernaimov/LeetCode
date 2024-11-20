def firstUniqChar(s):
    unique_list = [] #letcod
    unique_list2 = []
    for i in range(len(s)):
        if s[i] not in unique_list:
            unique_list.append(s[i])
        else:
            unique_list2.append(s[i])
    unique_list2 = list(dict.fromkeys(unique_list2))

    print(unique_list)
    print(unique_list2)
    for i in range(len(s)):
        if s[i] not in unique_list2 and s[i] in unique_list:
            return i
    return -1

print(firstUniqChar("dddccdbba"))