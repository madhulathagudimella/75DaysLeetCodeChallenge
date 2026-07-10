class Solution:
    def generateParenthesis(self,n):
        ans=[]
        def bt(s,o,c):
            if len(s)==2*n:
                ans.append(s)
                return
            if o<n:
                bt(s+"(",o+1,c)
            if c<o:
                bt(s+")",o,c+1)
        bt("",0,0)
        return ans