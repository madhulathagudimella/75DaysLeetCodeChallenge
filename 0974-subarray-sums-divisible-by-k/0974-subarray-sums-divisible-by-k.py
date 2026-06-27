class Solution:
    def subarraysDivByK(self,nums,k):
        d={0:1}
        s=0
        c=0
        for i in nums:
            s+=i
            r=s%k
            if r in d:
                c+=d[r]
                d[r]+=1
            else:
                d[r]=1
        return c