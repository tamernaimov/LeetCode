def intersection(nums1,nums2):
    nums = []
    for i in range (len(nums1)):
        for j in range (len(nums2)):
            if nums1[i] == nums2[j]:
                nums.append(nums1[i])
    unique_list = list(set(nums))

    return unique_list


print(intersection([5,1,2,3],[1,7,7,5]))
