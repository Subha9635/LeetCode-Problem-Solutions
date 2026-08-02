class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generator("",n,result)
        return result
    
    def validity(self, string:str):  #Checks the validity whether no of "(" is equal to ")" or not
        balance = 0
        for char in string:
            if char == "(":
                balance += 1
            else:
                balance -= 1
            if balance<0:
                return False
        return balance == 0
    
    def generator(self, curr:str, n:int, res:List[int]):
        if len(curr) == 2*n:
            if self.validity(curr):
                res.append(curr)
            return
        self.generator(curr+"(",n,res)
        self.generator(curr+")",n,res)