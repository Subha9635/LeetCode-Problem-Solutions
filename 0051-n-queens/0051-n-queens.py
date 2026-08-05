class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []
        lefthash, upperdiag, lowerdiag = [0]*n, [0]*(2*n-1), [0]*(2*n-1)
        self.solver(0, board, ans, n, lefthash, lowerdiag, upperdiag)
        return ans

    def solver(self, col, board, ans, n, lefthash, lowerdiag, upperdiag):
        if col == n:
            ans.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            if lefthash[row] == 0 and lowerdiag[row+col] == 0 and upperdiag[(n-1)+(col-row)] == 0:
                lefthash[row] = 1
                lowerdiag[row+col] = 1
                upperdiag[(n-1)+(col-row)] = 1
                board[row][col] = "Q"
                self.solver(col+1,board,ans,n,lefthash,lowerdiag,upperdiag)
                board[row][col] = "."
                lefthash[row] = 0
                lowerdiag[row+col] = 0
                upperdiag[(n-1)+(col-row)] = 0