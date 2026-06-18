# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution:
    def guessNumber(self,n):
        l,r=1,n
        while l<=r:
            m=(l+r)//2
            g=guess(m)
            if g==0:
                return m
            elif g<0:
                r=m-1
            else:
                l=m+1