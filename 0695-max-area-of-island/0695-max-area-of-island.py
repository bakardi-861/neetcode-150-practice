class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # max ones in an island
        dirs = [(0,1),(0,-1,),(1,0),(-1,0)]
        rows,cols = len(grid),len(grid[0])
        
        def dfs(r,c):
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] != 1:
                return 0

            grid[r][c] = 2
            area = 1
            for dr,dc in dirs:
                area += dfs(r+dr,c+dc)
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(dfs(r,c),max_area)
        return max_area