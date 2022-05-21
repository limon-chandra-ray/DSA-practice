def searchInsertPosition(nums,target):
    first_index = 0
    last_index = len(nums) - 1
    while first_index <= last_index:
        mid = (first_index+last_index) //2
        if nums[mid] < target:
            first_index = mid +1
        elif nums[mid] > target:
            last_index = mid - 1
        else:
            nums.insert(mid,target)
            return mid

    nums.append(target)
    nums.sort()
    return nums.index(target)

nums =  [1,3,5,6]
target = 7
x = searchInsertPosition(nums,target)
print(x)