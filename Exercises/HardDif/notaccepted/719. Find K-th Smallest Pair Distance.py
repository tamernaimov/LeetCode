def smallestDistancePair(nums,k):
    pairs = []
    results = []

    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            pairs.append([nums[i],nums[j]])

    print(pairs)
    for i in range (len(pairs)):
        if pairs[i][0] - pairs[i][1] < 0:
            results.append((pairs[i][0] - pairs[i][1]) * -1)
        else:
            results.append((pairs[i][0] - pairs[i][1]))

    results.sort()
    return results[k-1]


print(smallestDistancePair([1,3,1],2)) #memory limit exceeded but works :D - f
