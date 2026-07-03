class Solution:
    def maximumUniqueSubarray(self,nums):
        l=0
        s=0
        ans=0
        st=set()
        for r in range(len(nums)):
            while nums[r]in st:
                st.remove(nums[l])
                s-=nums[l]
                l+=1
            st.add(nums[r])
            s+=nums[r]
            ans=max(ans,s)
        return ans