def singleNumber(nums):
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1

    print(hashmap)
    for idx, (key, value) in enumerate(hashmap.items()):
        if value == 1:
            return key
