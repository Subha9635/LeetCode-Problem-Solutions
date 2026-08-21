class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix, suffix = [0]*n, [0]*n
        self.prefixmax(height,prefix)
        self.suffixmax(height,suffix)
        total = 0
        for i in range(n):
            leftmax = prefix[i]
            rightmax = suffix[i]
            if height[i] < leftmax and height[i] < rightmax:
                total += min(leftmax,rightmax) - height[i]
        return total
    
    
    def prefixmax(self, height,prefix):
        prefix[0] = height[0]
        for i in range(1,len(height)):
            prefix[i] = max(prefix[i-1], height[i])
    
    def suffixmax(self, height,suffix):
        suffix[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])