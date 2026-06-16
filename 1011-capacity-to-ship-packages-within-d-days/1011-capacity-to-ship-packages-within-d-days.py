class Solution:
    def shipWithinDays(self,weights,days):
        l,r=max(weights),sum(weights)
        while l<r:
            m=(l+r)//2
            d=1
            cur=0
            for w in weights:
                if cur+w>m:
                    d+=1
                    cur=0
                cur+=w
            if d<=days:
                r=m
            else:
                l=m+1
        return l