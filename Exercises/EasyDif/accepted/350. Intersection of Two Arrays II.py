def intersect(nums1,nums2):
    unique_list = []
    if len(nums1) > len(nums2) :
        for i in range (len(nums2)):
            if nums2[i] in nums1:
                unique_list.append(nums2[i])
                nums1.remove(nums2[i])

    else:
        for i in range (len(nums1)):
            if nums1[i] in nums2:
                unique_list.append(nums1[i])
                nums2.remove(nums1[i])


    return unique_list


print(intersect([3,1,2],[1,1]))
