def firstMissingPositive(nums):
    for i in range (1,len(nums)+1):
        if i not in nums:
            return i
    return max(nums)+1

print(firstMissingPositive([1,1000]))
