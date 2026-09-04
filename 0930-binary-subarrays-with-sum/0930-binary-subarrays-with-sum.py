class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        return self.finder(nums,goal)-self.finder(nums,goal-1)

    def  finder(self, nums, goal):    #Finds out the count of subarrays with sum <= goal
        l, r, sum, count = 0, 0, 0, 0
        while r<len(nums):
            if goal < 0:    #As goal-1 will be given to the function and the goal could be 0 and the elements will only be binary so <0 sum is not possible
                return 0
            sum += nums[r]
            while sum > goal:
                sum -= nums[l]
                l += 1
            count += (r-l+1)
            r += 1
        return count