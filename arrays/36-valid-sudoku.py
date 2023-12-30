# https://leetcode.com/problems/valid-sudoku/submissions/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # probably should use a hash set to track the whole grid and its values

        def check_row(board, row_number) -> bool:
            existing_nums = {}
            for val in board[row_number]:
                if val in existing_nums.keys(): return False
                if val != ".":
                    existing_nums[val] = True
            return True
        def check_col(board, col_number) -> bool:
            existing_nums = {}
            for i in range(0, 9):
                val = board[i][col_number]
                if val in existing_nums.keys(): return False
                if val != ".":
                    existing_nums[val] = True
            return True
        def check_square(board, start_x, start_y) -> bool:
            existing_nums = {}
            for x in range(start_x, start_x + 3):
                for y in range(start_y, start_y + 3):
                    val = board[x][y]
                    if val in existing_nums.keys(): return False
                    if val != ".":
                        existing_nums[val] = True
            return True

        # Easy once you have the methods written for each sub problem

        for row in range(0,9):
            if not check_row(board, row): return False
        for col in range(0,9):
            if not check_col(board, col): return False
        starts = (0, 3, 6)
        for x in starts:
            for y in starts:
                if not check_square(board, x, y): return False
        return True
