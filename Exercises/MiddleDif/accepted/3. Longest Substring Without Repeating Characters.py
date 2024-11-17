def lengthOfLongestSubstring(s):
    chars = list(s)
    biggest = 0
    for i in range (len(chars)):
        counter = 0
        unique_list = []
        for j in range (i,len(chars)):
            if chars[j] not in unique_list:
                unique_list.append(chars[j])
                counter +=1
            else:
                break
        if counter > biggest:
            biggest = counter
    return biggest

print(lengthOfLongestSubstring("abcabcbb"))