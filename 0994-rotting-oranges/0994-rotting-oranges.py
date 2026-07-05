from collections import deque

class Solution:
    def orangesRotting(self,grid):
        r=len(grid)
        c=len(grid[0])
        q=deque()
        fresh=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        t=0
        d=[[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh:
            for _ in range(len(q)):
                x,y=q.popleft()
                for dx,dy in d:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<r and 0<=ny<c and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        fresh-=1
                        q.append((nx,ny))
            t+=1
        return t if fresh==0 else -1