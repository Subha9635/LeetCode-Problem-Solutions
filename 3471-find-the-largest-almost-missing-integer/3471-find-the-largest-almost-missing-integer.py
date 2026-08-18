class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        counts = {} #Empty Hashtable

        for num in nums:
            counts[num] = counts.get(num,0)+1
        
        if k == len(nums):
            return max(nums)
        
        if k == 1:
            maxval = -1
            for num,freq in counts.items():
                if freq == 1:
                    maxval = max(maxval,num)
            return maxval
        
        ans = -1
        if counts.get(nums[0]) == 1:
            ans =  max(ans,nums[0])
        if counts.get(nums[-1]) == 1:
            ans = max(ans,nums[-1])
        return ans