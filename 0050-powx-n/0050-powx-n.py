class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n<0:
            y = -1*n
        else:
            y = n
        while y>0:
            if y%2 == 0:  #Even n
                x = x*x
                y = y/2
            else:   #Odd n
                result *= x
                y -= 1
        if n<0:
            result = 1/result
        return result