class Solution:
    def largestAltitude(self,gain):
        alt=0
        ans=0
        for g in gain:
            alt+=g
            ans=max(ans,alt)
        return ans