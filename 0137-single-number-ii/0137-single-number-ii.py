class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for bitindex in range(0,32): #iterates for all 32 bits of integer
            count = 0
            for i in range(0,len(nums)):   #Iterates the array
                if nums[i] & (1<<bitindex):
                    count += 1
            if count%3 == 1: #Means one element apperaing once
                ans = ans | (1<<bitindex)
            
        if ans >= 2**31:
            ans -= 2**32
        return ans