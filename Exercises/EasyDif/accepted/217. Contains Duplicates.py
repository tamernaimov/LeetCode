def containsDuplicate( nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False  #


print(containsDuplicate([4,1,2,10]))