class Solution:
    def reversePrefix(self,word,ch):
        i=word.find(ch)
        if i==-1:
            return word
        return word[:i+1][::-1]+word[i+1:]