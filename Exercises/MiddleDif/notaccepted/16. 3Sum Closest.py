def threeSumClosest(nums, target):
    nums.sort()

    triplet = [nums[0], nums[1], nums[2]]
    closest = sum(triplet)


    for i in range(3, len(nums)):
        triplet.append(nums[i])
        triplet.pop(0)

        current_sum = sum(triplet)


        if abs(current_sum - target) < abs(closest - target):
            closest = current_sum

    return closest  # Return the closest sum found


print(threeSumClosest([4,0,5,-5,3,3,0,-4,-5],-2))

