class Solution:
    def intersection(self,nums):
        d={}
        n=len(nums)
        for arr in nums:
            for x in arr:
                d[x]=d.get(x,0)+1
        ans=[]
        for k,v in d.items():
            if v==n:
                ans.append(k)
        return sorted(ans)