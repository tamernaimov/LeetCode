def findDuplicate(nums):
    hashmap = {}

    for i in range(len(nums)):
        hashmap[nums[i]] = 0

    for i in range (len(nums)):
        hashmap[nums[i]] += 1
        if hashmap[nums[i]] >1:
            return nums[i]
    return hashmap

print(findDuplicate([3,1,3,4,2]))