class Solution:
    def longestNiceSubstring(self,s):
        if len(s)<2:
            return ""
        st=set(s)
        for i,c in enumerate(s):
            if c.lower()in st and c.upper()in st:
                continue
            l=self.longestNiceSubstring(s[:i])
            r=self.longestNiceSubstring(s[i+1:])
            if len(l)>=len(r):
                return l
            return r
        return s