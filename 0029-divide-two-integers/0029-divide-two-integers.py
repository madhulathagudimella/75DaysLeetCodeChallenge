class Solution:
    def divide(self,dividend,divisor):
        if dividend==-2**31 and divisor==-1:
            return 2**31-1

        sign=1
        if (dividend<0 and divisor>0) or (dividend>0 and divisor<0):
            sign=-1

        a=abs(dividend)
        b=abs(divisor)
        ans=0

        while a>=b:
            temp=b
            count=1

            while a>=(temp<<1):
                temp<<=1
                count<<=1

            a-=temp
            ans+=count

        if sign==-1:
            return -ans
        return ans