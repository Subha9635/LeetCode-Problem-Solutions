class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xorvalue = x^y
        count = 0 
        while xorvalue != 0:
            xorvalue = xorvalue & (xorvalue-1)
            count += 1
        return count