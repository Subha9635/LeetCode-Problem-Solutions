class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.summer(k,n,1,[],res)
        return res
        
    def summer(self, k:int, target:int, ind:int, listt:List[int], res:List[int]):
        if target == 0 and len(listt)==k:
            res.append(list(listt))
            return
        if target <= 0 or len(listt)>k:
            return
        for i in range(ind,10):
            if i <= target:
                listt.append(i)
                self.summer(k,target-i,i+1,listt,res)
                listt.pop()
            else:
                break