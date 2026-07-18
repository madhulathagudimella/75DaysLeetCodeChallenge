class Solution:
    def rotateTheBox(self, box):
        m=len(box)
        n=len(box[0])
        for r in range(m):
            empty=n-1
            for c in range(n-1,-1,-1):
                if box[r][c]=='*':
                    empty=c-1
                elif box[r][c]=='#':
                    box[r][c]='.'
                    box[r][empty]='#'
                    empty-=1
        ans=[['']*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                ans[j][m-1-i]=box[i][j]
        return ans