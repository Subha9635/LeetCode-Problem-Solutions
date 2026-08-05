class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def dfs(i, j, ind):
            if ind == len(word):  #Found the complete word ind standing at len(word) which is only possible if thw whole word has been found
                return True
            if i<0 or j<0 or i>=row or j>=col or board[i][j] != word[ind]:
                return False
            temp = board[i][j]
            board[i][j] = "#"  #Marks the visited element as not to be considered twice
            found = (dfs(i,j+1,ind+1) or dfs(i,j-1,ind+1) or dfs(i+1,j,ind+1) or dfs(i-1,j,ind+1))
            board[i][j] = temp
            return found

        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False