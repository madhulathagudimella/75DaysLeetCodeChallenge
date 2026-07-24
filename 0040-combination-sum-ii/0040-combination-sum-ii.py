class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans=[]
        path=[]
        def backtrack(start,total):
            if total==target:
                ans.append(path[:])
                return
            if total>target:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,total+candidates[i])
                path.pop()
        backtrack(0,0)
        return ans