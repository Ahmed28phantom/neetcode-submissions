class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = True

        # checking rows
        for i in range(9):
            set1 = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in set1:
                        result = False
                    set1.add(board[i][j])

        # checking columns
        for j in range(9):
            set2 = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in set2:
                        result = False
                    set2.add(board[i][j])
        
        # checking boxes
        boxes = {}
        for i in range(9):
            for j in range(9):
                key = (i//3, j//3)

                if board[i][j] != ".":
                    if key not in boxes:
                        boxes[key] = set()
                    if board[i][j] in boxes[key]:
                        result = False
                    boxes[key].add(board[i][j])
        return result