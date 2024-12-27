def maxSlidingWindow(nums,k):
    unique_list = []
    l = 0
    r = l+k

    while r < len(nums)+1:
        unique_list.append(max(nums[l:r]))
        l += 1
        r += 1
    return unique_list


print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))