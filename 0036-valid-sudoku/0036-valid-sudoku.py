class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row set, col set, box set
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".": continue
                box_index = (r//3) * 3 + (c//3)

                if num in row_set[r] or num in col_set[c] or num in box_set[box_index]:
                    return False

                row_set[r].add(num)
                col_set[c].add(num)
                box_set[box_index].add(num)
        return True