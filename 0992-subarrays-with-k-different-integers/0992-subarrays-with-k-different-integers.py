class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.counter(nums,k)-self.counter(nums,k-1)
    
    def counter(self, nums:List[int], k:int):       #Counts subarrays with <=k distinct integers
        l, r = 0, 0
        count = 0
        hash = {}

        while r < len(nums):
            hash[nums[r]] = hash.get(nums[r],0)+1
            while len(hash) > k:
                hash[nums[l]] -= 1
                if hash[nums[l]] == 0:
                    del hash[nums[l]]
                l += 1
            count += (r-l+1)
            r += 1
        return count