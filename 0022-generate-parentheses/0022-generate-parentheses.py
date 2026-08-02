class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack("",0,0,n,result)
        return result
    
    def backtrack(self, curr:str, openn:int, close:int, n:int, res:List[str]):
        if len(curr) == 2*n:
            res.append(curr)
            return
        if openn<n:
            self.backtrack(curr+"(", openn+1, close, n, res)
        if close<openn:
            self.backtrack(curr+")", openn, close+1, n,res)