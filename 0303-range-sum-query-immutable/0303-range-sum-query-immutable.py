class NumArray:
    def __init__(self,nums):
        self.pre=[0]
        for n in nums:
            self.pre.append(self.pre[-1]+n)
    def sumRange(self,left,right):
        return self.pre[right+1]-self.pre[left]