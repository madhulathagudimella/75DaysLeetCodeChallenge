class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res=[]
        def dfs(index,path):
            res.append(path[:])
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        dfs(0,[])
        return res