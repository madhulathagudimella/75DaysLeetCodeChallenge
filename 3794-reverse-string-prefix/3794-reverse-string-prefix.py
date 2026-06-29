class Solution:
    def reversePrefix(self,s,k):
        a=list(s)
        l,r=0,k-1
        while l<r:
            a[l],a[r]=a[r],a[l]
            l+=1
            r-=1
        return "".join(a)