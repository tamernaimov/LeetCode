import math
def numSubarrayProductLessThanK(nums,k):
    result = 0
    for i in range (len(nums)):
        if nums[i] < k:
            result+=1

    l = 0
    r = 2
    while l < len(nums)-1 :
        windowed = nums[l:r]
        if math.prod(windowed) < k and len(windowed) > 1:
            result+=1
            r+=1
        elif math.prod(windowed) >= k  and len(windowed) > 1:
            l+=1
            r = l+2
        if r > len(nums)-1:
            l+=1
            r = l+2

    return result


print(numSubarrayProductLessThanK([10,5,2,12,13,6,14],100)) #time exceeded