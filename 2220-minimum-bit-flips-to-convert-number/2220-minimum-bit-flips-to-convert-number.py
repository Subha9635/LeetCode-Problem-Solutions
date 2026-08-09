class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xorvalue = start ^ goal #Ensures only position flipping required bits have set
        count = 0
        while xorvalue != 0:
            xorvalue = xorvalue & (xorvalue-1) #Removes rightmost set bit
            count += 1
        return count