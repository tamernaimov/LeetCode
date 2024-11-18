from ctypes import c_wchar


def searchRange(nums,target):
    left = 0
    right = len(nums)-1
    counterForLeft = 0
    counterForRight = 0
    middleAnswer = 0
    print(nums)
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] > target:
            right = middle-1
        elif nums[middle] < target:
            left = middle+1
        else: #TARGET FOUND
            print(f"sredata e {middle}")
            middleAnswer = middle
            m = middle
            t = target

            if middle == len(nums) -1:
                break
            if nums[middle] == nums[middle-1]: #Do ANOTHER check here
                counterForLeft -= 1
                while t == target: #True,
                    if m > -1: #2 puti po logicka //
                        counterForLeft += 1
                        m -= 1 #3
                        t = nums[m] # nums[2]
                    else:
                        break
            print(counterForLeft)
            if counterForLeft < 0:
                counterForLeft = 0

            m = middle
            t = target

            if nums[middle] == nums[middle+1]: # True
                counterForRight -= 1
                while t == target:  # True,
                    if m < len(nums):  #0,2
                        counterForRight += 1
                        m += 1
                        if m < len(nums):
                            t = nums[m] #
                    else:
                        break
            print(counterForRight)
            if counterForRight < 0 :
                counterForRight = 0
            break
    if left > right:
        return [-1,-1]

    positions = []
    positions.append(middleAnswer-counterForLeft)
    positions.append(middleAnswer+counterForRight)

    return positions

print(searchRange([1,2,3,3,3,3,4],3))