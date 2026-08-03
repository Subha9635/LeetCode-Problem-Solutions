class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
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
        self.combinator(arr, target - arr[ind], ind+1, listt, res, n)
        listt.pop()

        next_ind = ind + 1
        while next_ind < n and arr[next_ind] == arr[ind]:
            next_ind += 1

        self.combinator(arr, target, next_ind, listt, res, n)