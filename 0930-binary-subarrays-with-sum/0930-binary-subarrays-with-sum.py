class Solution:
    def numSubarraysWithSum(self,nums,goal):
        d={0:1}
        s=0
        ans=0
        for n in nums:
            s+=n
            if s-goal in d:
                ans+=d[s-goal]
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return ans