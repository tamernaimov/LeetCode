def topKFrequent(nums,k):
    hashmap = {}

    for num in nums:
        hashmap[num] = 0
    for num in nums:
        hashmap[num] +=1

    freq = []
    sorter = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
    print(sorter)
    t = 0
    for num in sorter:
        freq.append(num)
        t+=1
        if t == k:
            return freq


print(topKFrequent([1,1,1,2,2,3,3,3,3,3,3,3],2))