class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each row must contain the digits 1-9 without repetition.
        # Each col must contain the digits 1-9 without repetition.
        # Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        # A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        # Only the filled cells need to be validated according to the mentioned rules.
        # WE DON'T NEED TO SOLVE, ONLY VALIDATE CURRENT BOARD STATE

        # create a set for each row and col, and sub box to store each digit.
        # 3x3 box index: box_index = (row // 3, col // 3)

        ROWS,COLS = len(board), len(board[0])
        row_map, col_map, box_map = defaultdict(set), defaultdict(set), defaultdict(set)
        
        # skip if '.'
        # check each row
        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == '.':
                    continue
                if val in row_map[r] or val in col_map[c] or val in box_map[(r // 3, c // 3)]:
                    return False
                row_map[r].add(val)
                col_map[c].add(val)
                box_map[(r // 3, c // 3)].add(val)
        return True
