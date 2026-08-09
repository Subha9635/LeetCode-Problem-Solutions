class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #n&(n-1) == 0: #It means only one set bit is 
        #n>0 means no number <= 0 is checked
        return n>0 and n&(n-1) == 0