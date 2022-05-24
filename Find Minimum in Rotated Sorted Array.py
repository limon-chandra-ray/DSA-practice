class Solution:
    def findMin(self, nums):
        nums.sort()
        return nums[0]



nums = [3, 4, 5, 1, 2]
solution = Solution()
x = solution.findMin(nums)
print(x)