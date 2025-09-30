class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        rows,cols = len(grid),len(grid[0])

        def dfs(r,c):
            if min(r,c) < 0 or r >= rows or c >= cols or not grid[r][c]:
                return 0
            
            grid[r][c] = 0

            area = 1
            for dr,dc in dirs:
                area += dfs(dr+r,dc+c)
            return area        

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res,dfs(r,c))
        return res