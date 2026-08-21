class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suffix = [0]*n
        self.suffixmax(height,suffix)
        leftmax = height[0]
        total = 0
        for i in range(n):
            rightmax = suffix[i]
            leftmax = max(leftmax,height[i]) #Calculating leftmax on the run
            if height[i] < leftmax and height[i] < rightmax:
                total += min(leftmax,rightmax) - height[i]
        return total
    
    def suffixmax(self, height,suffix):
        suffix[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            suffix[i] = max(suffix[i+1],height[i])