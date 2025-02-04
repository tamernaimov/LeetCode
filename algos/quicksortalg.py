def partition(nums, low, high):
    pivot = nums[high]

    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:

            i = i + 1

            (nums[i], nums[j]) = (nums[j], nums[i])

    (nums[i + 1], nums[high]) = (nums[high], nums[i + 1])

    return i + 1


def quickSort(nums, low, high):
    if low < high:

        pi = partition(nums, low, high)

        quickSort(nums, low, pi - 1)

        quickSort(nums, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)