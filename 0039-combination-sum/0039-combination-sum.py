class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        self.combinator(candidates, target, 0, [], res, n)
        return res
        
    
    def combinator(self, arr:List[int], target:int, ind:int, listt:List[int], res:List[int], n:int):
        if target == 0:
            res.append(listt.copy())
            return
        if ind == n or target<0:
            return
            
        listt.append(arr[ind])
        self.combinator(arr, target - arr[ind], ind, listt, res, n)
        listt.pop()
        self.combinator(arr, target, ind+1, listt, res, n)