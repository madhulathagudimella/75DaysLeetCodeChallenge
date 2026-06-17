class Solution:
    def splitArray(self,nums,k):
        l,r=max(nums),sum(nums)
        while l<r:
            m=(l+r)//2
            cnt=1
            cur=0
            for n in nums:
                if cur+n>m:
                    cnt+=1
                    cur=0
                cur+=n
            if cnt<=k:
                r=m
            else:
                l=m+1
        return l