def merge( nums1 , m, nums2, n):
    for i in range (len(nums2)):
        nums1[len(nums2)+ i] = nums2[i]

    nums1.sort()
    return nums1


print(merge([1,2,3,0,0,0],3,[2,5,6],3)) # [1,2,2,3,5,6]
