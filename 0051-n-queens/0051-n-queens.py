class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []
        self.solver(0,board,ans,n)
        return ans
        

    def solver(self, col, board, ans, n):
        if col == n:
            ans.append(["".join(row) for row in board])
            return
        for row in range(n):
            if self.isSafe(row,col,board,n):
                board[row][col] = "Q"
                self.solver(col+1,board,ans,n)
                board[row][col] = "."

    def isSafe(self, row, col, board, n):
        duprow, dupcol = row, col
        while row>=0 and col>= 0:  #Checks Upper Diagonal
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        
        row, col = duprow, dupcol
        while row<n and col>=0:  #Checks lowerd diagonal
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1

        row, col = duprow, dupcol
        while col>=0:  #Checks Left side
            if board[row][col] == "Q":
                return False
            col -= 1
        return True