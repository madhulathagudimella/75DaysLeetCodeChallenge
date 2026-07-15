class Solution:
    def maxDistance(self,position,m):
        position.sort()
        def canPlace(dist):
            cnt=1
            last=position[0]
            for i in range(1,len(position)):
                if position[i]-last>=dist:
                    cnt+=1
                    last=position[i]
                    if cnt>=m:
                        return True
            return False
        l,r=1,position[-1]-position[0]
        ans=1
        while l<=r:
            mid=(l+r)//2
            if canPlace(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans