class Solution:
    def rotateTheBox(self, grid: List[List[str]]) -> List[List[str]]:
       # Step 1: Move stones to the right in each row
    # r   [".",".","*","#"]
    #       c
    #                   k
        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            k = cols - 1
            for c in range(cols - 1, -1, -1):
                if grid[r][c] == '*':
                    k = c - 1  # reset k position to left of '*'
                elif grid[r][c] == '#':
                    if k != c:
                        grid[r][k], grid[r][c] = '#', '.'
                    k -= 1

        # Step 2: Rotate the box 90 degrees clockwise
        rotated = [ [0] * rows for _ in range(cols) ]

        

        for r in range(rows):
            for c in range(cols):
                rotated[c][rows - 1 - r] = grid[r][c]

        return rotated