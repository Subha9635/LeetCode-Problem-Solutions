class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        l, r = 0, 0
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros>k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen