class Solution:
    def gcdValues(self, nums, queries):
        mx=max(nums)
        cnt=[0]*(mx+1)
        for x in nums:
            cnt[x]+=1
        divCnt=[0]*(mx+1)
        for g in range(1,mx+1):
            for j in range(g,mx+1,g):
                divCnt[g]+=cnt[j]
        exact=[0]*(mx+1)
        for g in range(mx,0,-1):
            c=divCnt[g]
            exact[g]=c*(c-1)//2
            for k in range(g*2,mx+1,g):
                exact[g]-=exact[k]
        pref=[0]*(mx+1)
        for g in range(1,mx+1):
            pref[g]=pref[g-1]+exact[g]
        ans=[]
        for q in queries:
            l,r=1,mx
            while l<r:
                mid=(l+r)//2
                if pref[mid]>q:
                    r=mid
                else:
                    l=mid+1
            ans.append(l)
        return ans