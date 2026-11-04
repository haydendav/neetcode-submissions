class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set) #only distict vals can live in each row, column, and square
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or #if the value already exists in the row, col, or square then return false
                    board[row][col] in cols[col] or
                    board[row][col] in squares[(row // 3, col // 3)]):
                    return False
                
                cols[col].add(board[row][col]) #otherwise add it to the sets
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col]) #and anything // 3 will be in the same square 
        
        return True