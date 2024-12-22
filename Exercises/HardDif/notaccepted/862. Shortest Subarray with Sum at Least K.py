def shortestSubarray(nums,k):
    subarrays = []
    if len(nums) == 1:
        if nums[0] >= k:
            return 1
        else:
            return -1

    for i in range (len(nums)):
        cur = nums[i]
        subarray = [nums[i]]
        for j in range (i, len(nums)-1):
            if cur < k:
                cur += nums[j + 1]
                subarray.append(nums[j + 1])

            if cur>= k:
                subarrays.append(subarray)
                break


    if not subarrays:
        return -1
    for i in range (len(subarrays)):
        subarrays[i] = len(subarrays[i])
    return min(subarrays)

print(shortestSubarray([2,1,4,1],3))


