def trap(height):
    if not height:
        return 0
    l = 0
    r = len(height)-1
    res = 0

    leftMax = height[l]
    rightMax = height[r]

    while l < r:
        if leftMax < rightMax:
            l+=1
            leftMax = max(leftMax,height[l])
            res += leftMax - height[l]

        else:
            r-=1
            rightMax = max(rightMax,height[r])
            res += rightMax - height[r]

    return res


print(trap([0,1,0,2,1,0,1,3,2,1,2]))