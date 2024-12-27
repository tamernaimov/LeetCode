def firstMissingPositive(nums):
    pos = []
    for i in range (len(nums)):
        if nums[i] > 0:
            pos.append(nums[i])
    if len(pos) == 1 and pos[0] != 1:
        return 1
    if len(pos) == 1:
        return 2

    pos = list(dict.fromkeys(pos))
    pos.sort()

    for i in range (0,len(pos)):
        if i+1 != pos[i]:
            return i+1
    return len(pos)+1


print(firstMissingPositive([2,2]))