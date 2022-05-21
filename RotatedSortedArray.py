def SortedArray(nums,target):
    left_index = 0
    right_index = len(nums) -1
    nums_sort = nums.copy()
    nums_sort.sort()
    mid_index = 0
    while left_index <= right_index:
        mid = (right_index+left_index)//2
        if nums_sort[mid] < target:
            left_index = mid + 1
        elif nums_sort[mid] > target:

            right_index = mid - 1
        else:
            values = nums_sort[mid]
            x = nums.index(values)
            return x
    return -1

    # if left_index == right_index:
    #     values = nums_sort[left_index]
    #     x = nums.index(values)
    #     return x
    # else:
    #     return -1




nums = [4,5,6,7,0,1,2]
target = 0

x = SortedArray(nums,target)
print(x)