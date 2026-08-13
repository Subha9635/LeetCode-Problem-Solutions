class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        XOR = 0 #Xor of all numbers
        bucket1, bucket2 = 0, 0 #bucket1 stores all the element whose rightmost bit is set & bucket2 stores all the elemmnts whose rightmost bit is not set
        for num in nums:
            XOR ^= num
        
        rightmost = (XOR^(XOR-1)&XOR) #Used to figure out whether the rightmost bit is set or not
        for num in nums:
            if rightmost&num != 0:
                bucket1 ^= num
            else:
                bucket2 ^= num
        
        return [bucket1,bucket2]