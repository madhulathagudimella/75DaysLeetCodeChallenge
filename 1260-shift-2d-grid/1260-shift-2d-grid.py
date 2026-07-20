class Solution:
    def shiftGrid(self,grid,k):
        m=len(grid)
        n=len(grid[0])
        total=m*n
        k%=total
        ans=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx=i*n+j
                newidx=(idx+k)%total
                r=newidx//n
                c=newidx%n
                ans[r][c]=grid[i][j]
        return ans