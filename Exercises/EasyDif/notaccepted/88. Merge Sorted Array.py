def merge( nums1 , m, nums2, n):
    nums1 = nums1[:m]
    nums2 = nums2[:n]

    for i in range (len(nums2)):
        nums1.append(nums2[i])

    nums1.sort()
    return nums1


print(merge([0],0,[1],1)) # [1,2,2,3,5,6]
