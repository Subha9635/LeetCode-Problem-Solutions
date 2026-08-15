class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        m = n
        n = abs(n)
        while n>0:
            if n%2 == 1: #If power is odd
                ans *= x
                n -= 1
            else: #if power is even
                x *= x
                n = n//2
        if m<0:
            return 1/ans
        return ans