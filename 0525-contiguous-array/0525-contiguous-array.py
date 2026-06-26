class Solution(object):
    def findMaxLength(self, nums):
        d={0:-1}
        s=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                s-=1
            else:
                s+=1
            if s in d:
                ans=max(ans,i-d[s])
            else:
                d[s]=i
        return ans
        