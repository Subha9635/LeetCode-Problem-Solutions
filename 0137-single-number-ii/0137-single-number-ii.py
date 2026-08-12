class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0 #Declaring two buckets
        """
        num will go to ones if it is not in twos
        num will go to twos if it is in ones
        Another bucket thrice will be needed iff the thrice appearing elements are required to be given as output
        """
        for num in nums:
            ones = (ones^num) & ~twos
            twos = (twos^num) & ~ones
        return ones