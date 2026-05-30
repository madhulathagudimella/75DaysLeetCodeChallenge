from typing import List

class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        m, n = len(h), len(h[0])
        p, a = set(), set()

        def dfs(r, c, vis):
            vis.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in vis and h[nr][nc] >= h[r][c]:
                    dfs(nr, nc, vis)

        for i in range(m):
            dfs(i, 0, p)
            dfs(i, n - 1, a)

        for j in range(n):
            dfs(0, j, p)
            dfs(m - 1, j, a)

        return [[r, c] for r in range(m) for c in range(n) if (r, c) in p & a]