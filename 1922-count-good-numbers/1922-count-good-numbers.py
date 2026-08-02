class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9+7)
        evencount = (n+1)//2
        oddcount = n//2
        return (pow(5,evencount,MOD)*pow(4,oddcount,MOD)%MOD)