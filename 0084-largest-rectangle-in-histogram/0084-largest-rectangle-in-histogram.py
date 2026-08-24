class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                element = stack[-1]
                stack.pop()
                NSE = i
                PSE = -1 if not stack else stack[-1]
                maxarea = max(maxarea, heights[element]*(NSE-PSE-1))
            stack.append(i)
        
        while stack:
            NSE = len(heights)
            element = stack[-1]
            stack.pop()
            PSE = -1 if not stack else stack[-1]
            maxarea = max(maxarea, heights[element]*(NSE-PSE-1))
        
        return maxarea