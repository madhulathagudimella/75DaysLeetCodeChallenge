class Solution:
    def singleNumber(self,nums):
        d={}
        for n in nums:
            d[n]=d.get(n,0)+1
        ans=[]
        for k,v in d.items():
            if v==1:
                ans.append(k)
        return ans