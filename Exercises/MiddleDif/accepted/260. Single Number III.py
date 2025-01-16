def singleNumber( nums):
    hashmap = {}
    res = []
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1

    print(hashmap)
    for idx, (key, value) in enumerate(hashmap.items()):
        if value == 1:
            res.append(key)
    return res

print(singleNumber([5,4,1,1,5]))