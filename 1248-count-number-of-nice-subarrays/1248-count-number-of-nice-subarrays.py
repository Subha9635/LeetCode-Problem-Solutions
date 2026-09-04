class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.finder(nums,k)-self.finder(nums,k-1)
    
    def finder(self, nums, goal):
        l, r = 0, 0
        sum, count = 0, 0
        while r < len(nums):
            if goal < 0:
                return 0
            sum += nums[r]%2 #Converts odds to 1 and evens to 0
            while sum > goal:
                sum -= nums[l]%2
                l += 1
            count += (r-l+1)
            r += 1
        return count 