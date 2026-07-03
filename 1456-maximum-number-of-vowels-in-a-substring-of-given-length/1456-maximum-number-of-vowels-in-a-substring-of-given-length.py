class Solution:
    def maxVowels(self,s,k):
        v="aeiou"
        c=0
        for i in range(k):
            if s[i]in v:
                c+=1
        ans=c
        for i in range(k,len(s)):
            if s[i]in v:
                c+=1
            if s[i-k]in v:
                c-=1
            ans=max(ans,c)
        return ans