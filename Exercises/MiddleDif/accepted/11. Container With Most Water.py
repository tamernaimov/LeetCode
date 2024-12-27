def maxArea(height):
    maximum = 0
    l = 0
    r = len(height)-1

    while l < r:
        width = r-l
        curHeight = min(height[l],height[r])
        if width*curHeight > maximum:
            maximum = width*curHeight

        if height[l] < height[r]:
            l+=1
        elif height[r] < height[l]:
            r-=1
        else:
            l+=1
    return maximum



print(maxArea([1,1]))