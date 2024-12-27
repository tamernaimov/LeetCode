def alternatingSubarray( nums):
    the_truth = False
    max_counter = 0
    for i in range(len(nums)):
        counter = 0
        for j in range(i + 1, len(nums)):

            if nums[i] - nums[j] == -1 or nums[i] - nums[j] == 0:
                if nums[j] != nums[j - 1]:
                    the_truth = True
                    print(nums[j])
                    counter += 1
                else:
                    break
            else:
                break
        if counter > max_counter:
            max_counter = counter

    if the_truth:
        return max_counter + 1
    return -1


print(alternatingSubarray([1,2,1,2,1,2,1,2,1,2]))