class Solution(object):
    def subsets(self, nums):
        ans=[]
        path=[]
        def backtrack(start):
            ans.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ans