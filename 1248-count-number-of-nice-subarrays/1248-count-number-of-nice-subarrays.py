class Solution:
    def numberOfSubarrays(self,nums,k):
        d={0:1}
        odd=0
        ans=0
        for n in nums:
            if n%2==1:
                odd+=1
            if odd-k in d:
                ans+=d[odd-k]
            if odd in d:
                d[odd]+=1
            else:
                d[odd]=1
        return ans