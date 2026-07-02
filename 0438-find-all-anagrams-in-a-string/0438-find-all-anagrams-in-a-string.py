class Solution:
    def findAnagrams(self,s,p):
        if len(p)>len(s):
            return[]
        a=[0]*26
        b=[0]*26
        for c in p:
            a[ord(c)-97]+=1
        for i in range(len(p)):
            b[ord(s[i])-97]+=1
        ans=[]
        if a==b:
            ans.append(0)
        for i in range(len(p),len(s)):
            b[ord(s[i])-97]+=1
            b[ord(s[i-len(p)])-97]-=1
            if a==b:
                ans.append(i-len(p)+1)
        return ans