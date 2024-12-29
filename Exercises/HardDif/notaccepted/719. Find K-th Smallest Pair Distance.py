

def smallestDistancePair(nums,k):
    results = []

    for i in range (len(nums)):
        for j in range (i+1,len(nums)):
            if len(results) < k:
                results.append(abs(nums[i]-nums[j]))


    results.sort()
    print(results)
    return results[k-1]


print(smallestDistancePair([1,3,1,4],3))