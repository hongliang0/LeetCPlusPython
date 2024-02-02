class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create three dictionaries to store values
        row_dict = {}
        col_dict = {}
        grid_dict = {}
        for col in range(9):
            for row in range(9):
                # If value is non-zero
                if board[row][col] != ".":

                    # Check the row
                    if row not in row_dict:
                        row_dict[row] = set()
                        row_dict[row].add(board[row][col])
                    elif board[row][col] in row_dict[row]:
                        return False
                    else:
                        row_dict[row].add(board[row][col])

                    # Check the col
                    if col not in col_dict:
                        col_dict[col] = set()
                        col_dict[col].add(board[row][col])
                    elif board[row][col] in col_dict[col]:
                        return False
                    else:
                        col_dict[col].add(board[row][col])

                    # Check the grid by calculating the index
                    index = (row // 3) * 3 + col // 3
                    if index not in grid_dict:
                        grid_dict[index] = set()
                        grid_dict[index].add(board[row][col])
                    elif board[row][col] in grid_dict[index]:
                        return False
                    else:
                        grid_dict[index].add(board[row][col])
                else:
                    continue
        return True
