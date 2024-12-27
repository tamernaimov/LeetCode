def maxNumber(nums1,nums2,k):
    maxnum1 = 0
    maxnum2 = 0
    maxArr = []

    for i in range(len(nums1)):
        if nums1[i] > maxnum1:
            maxnum1 = nums1[i]

    for i in range (len(nums2)):
        if nums2[i] > maxnum2:
            maxnum2 = nums2[i]

    if maxnum1 > maxnum2:
        for i in range (len(nums1)):
            if nums1[i] > maxnum2:
                maxArr.append(nums1[i])
