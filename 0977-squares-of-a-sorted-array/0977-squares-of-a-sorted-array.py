class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        
        l, r = 0, n - 1
        
        for i in range(n - 1, -1, -1):
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res[i] = nums[l] * nums[l]
                l += 1
            else:
                res[i] = nums[r] * nums[r]
                r -= 1
        
        return res