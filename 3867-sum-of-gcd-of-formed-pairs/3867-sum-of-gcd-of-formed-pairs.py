class Solution:
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a
    def gcdSum(self,nums):
        pre=[]
        mx=0
        for x in nums:
            if x>mx:
                mx=x
            pre.append(self.gcd(x,mx))
        pre.sort()
        ans=0
        l,r=0,len(pre)-1
        while l<r:
            ans+=self.gcd(pre[l],pre[r])
            l+=1
            r-=1
        return ans