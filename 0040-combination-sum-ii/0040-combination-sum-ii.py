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
        for i in range(ind,n):
            if i>ind and arr[i] == arr[i-1]:
                continue
            if arr[i]>target:
                break
            listt.append(arr[i])
            self.combinator(arr, target - arr[i], i+1, listt, res, n)
            listt.pop()