def findMaxAverage(nums,k):
    max_avg = -2147483647
    i = 0

    while i < len(nums)-k+1:
        window = nums[i:k+i]
        cur_sum = sum(window)
        cur_avg = cur_sum / len(window)
        i+=1

        if cur_avg > max_avg:
            print(window)
            max_avg = cur_avg

    return max_avg

print(findMaxAverage([1,12,-5,-6,50,3],4))