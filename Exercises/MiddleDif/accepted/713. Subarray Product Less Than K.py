import math
def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    result = 0
    l = 0
    prod = 1
    r = 0

    while r < len(nums):
        prod *= nums[r]

        while prod >= k and l <= r:
            prod //= nums[l]
            l += 1

        result += (r - l + 1)

        r += 1


    return result
print(numSubarrayProductLessThanK([1,2,3],0))