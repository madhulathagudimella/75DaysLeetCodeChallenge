class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ans=0
        count=0
        for i in nums:
            if i == 1:
                count +=1
            else:
                ans=max(ans,count)
                count=0
        return max(ans,count)