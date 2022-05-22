class Solution:
    def isPerfectSquare(self, num: int) -> bool:
            if num == 1:
                return True
            left = 0
            right = num//2
            while right-left>1:
                mid= (right+left)//2
                if mid*mid == num:
                    return True
                elif mid*mid > num:
                    right = mid-1
                else:
                    left=mid
            if right*right == num:
                return True
            else:
                return False
num =36
solutionClass =Solution()
output = solutionClass.isPerfectSquare(num)
print(output)