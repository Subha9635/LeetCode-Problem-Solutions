class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        NSE = self.findNSE(heights)
        PSE = self.findPSE(heights)
        maxi = 0
        for i in range(len(heights)):
            maxi = max(maxi, heights[i]*(NSE[i]-PSE[i]-1))
        return maxi
    
    def findNSE(self, arr):
        n = len(arr)
        NSE = [n]*n
        stack = []
        i = n-1
        while i >= 0:
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if not stack:
                NSE[i] = n
            else:
                NSE[i] = stack[-1]
            stack.append(i)
            i -= 1
        return NSE
        
    def findPSE(self, arr):
        n = len(arr)
        PSE = [-1]*n
        stack = []
        i = 0
        while i < n:
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if not stack:
                PSE[i] = -1
            else:
                PSE[i] = stack[-1]
            stack.append(i)
            i += 1
        return PSE
