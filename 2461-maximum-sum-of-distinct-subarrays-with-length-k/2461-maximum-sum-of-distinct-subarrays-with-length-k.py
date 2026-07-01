class Solution:
    def maximumSubarraySum(self,nums,k):
        d={}
        s=0
        ans=0
        for i in range(len(nums)):
            s+=nums[i]
            d[nums[i]]=d.get(nums[i],0)+1
            if i>=k:
                s-=nums[i-k]
                d[nums[i-k]]-=1
                if d[nums[i-k]]==0:
                    del d[nums[i-k]]
            if i>=k-1 and len(d)==k:
                ans=max(ans,s)
        return ans
