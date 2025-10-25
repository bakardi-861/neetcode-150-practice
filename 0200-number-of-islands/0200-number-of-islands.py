class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        rows,cols = len(grid),len(grid[0])

        def dfs(r,c):
            if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] != "1":
                return 
            
            grid[r][c] = "2"

            for dr,dc in dirs:
                dfs(r+dr,c+dc)
            return

        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands
