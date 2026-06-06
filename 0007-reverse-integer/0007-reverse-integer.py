class Solution:
    def reverse(self,x):
        sign=1
        if x<0:
            sign=-1
            x=-x
        rev=0
        while x:
            rev=rev*10+x%10
            x//=10
        rev*=sign
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev