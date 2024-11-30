def findKthLargest(nums,k):
    nums.sort()
    return nums[len(nums)-k]



findKthLargest([3,2,1,5,6,4],2)