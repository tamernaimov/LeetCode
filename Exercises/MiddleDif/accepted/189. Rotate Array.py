def rotate(nums,k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

print(rotate([5,1,2,4],2))