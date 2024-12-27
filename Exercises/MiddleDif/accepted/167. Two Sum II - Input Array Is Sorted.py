def twoSum(numbers,target):
    l = 0
    r = len(numbers)-1
    while l<r:
        sumUp = numbers[l] + numbers[r]

        if sumUp > target:
            r-=1
        elif sumUp <target:
            l+=1
        else:
            return [l+1,r+1]

print(twoSum([2,7,11,15],9))