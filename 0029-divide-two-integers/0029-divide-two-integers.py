class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        
        #Handles Both cases where the result could be -ve
        sign = True #Means +ve
        if dividend<0 and divisor>0:
            sign = False
        if dividend>=0 and divisor<0:
            sign = False

        n, d = abs(dividend), abs(divisor)
        ans = 0
        while n>=d: #keep subtracting till dividend becomes smaller than divisor
            count = 0
            while n > (d<<(count+1)):   #Finds the largest one that could be subtracted; 1<<x == 2**x
                count += 1
            ans += 1<<count #Stores the 2**count value; 1<<count == 2**count
            n -= d<<count #dividend is reduced by the largest found; d*(2**count) == d<<count
        
        if ans>=2**31 and sign: #Does the boundary checking
            return 2**31-1
        elif ans>=2**31 and not sign:
            return -2**31
        
        if sign: #Assigns sign
            return ans
        else:
            return -ans