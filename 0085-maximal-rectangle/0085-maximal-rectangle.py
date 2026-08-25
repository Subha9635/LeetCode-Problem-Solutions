class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        This one boils down to Largest Histogram Problem; if for each individual row the bar height be known then its the same problem
        """
        row, col, maxarea = len(matrix), len(matrix[0]), 0
        prefixsum = [0]*col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    prefixsum[j] += 1
                else:
                    prefixsum[j] = 0
            maxarea = max(maxarea, self.lhist(prefixsum))
        return maxarea

    def lhist(self, arr):
        stack = []
        area = 0
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                elementindex = stack[-1]
                stack.pop()
                NSE = i
                PSE = -1 if not stack else stack[-1]
                area = max(area, arr[elementindex]*(NSE-PSE-1))
            stack.append(i)
        
        while stack:
            elementindex = stack[-1]
            stack.pop()
            NSE = len(arr)
            PSE = -1 if not stack else stack[-1]
            area = max(area, arr[elementindex]*(NSE-PSE-1))
        return area