def maxSlidingWindow(nums,k):
    l = 0
    r = l+k
    maximum = max(nums[l:k])
    unique_list = [maximum]
    cur = nums[l:k+1]
    # while r < len(nums)-1:
    #     l+=1
    #     r+=1
    #     cur.append(nums[r])
    #     del cur[l]
    #     print(cur)


    del cur[1]
    print(cur)
    return unique_list

print(maxSlidingWindow([3,1,-1,-3,5,3,6,7],3)) #[3,1,5,5,6,7]