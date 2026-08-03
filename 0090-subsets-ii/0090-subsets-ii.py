class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.subsequences(nums,0,[],res)
        return res
        
    def subsequences(self,arr,ind,listt,res):
        res.append(listt.copy())
        for i in range(ind,len(arr)):
            if i != ind and arr[i] == arr[i-1]:
                continue
            listt.append(arr[i])
            self.subsequences(arr,i+1,listt,res)
            listt.pop()