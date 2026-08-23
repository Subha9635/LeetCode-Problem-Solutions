class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return self.largestsum(nums) - self.smallestsum(nums) #This problem boils down to combination of Sum of Subarray maximums and Sum of Subarray minimums
    
    def largestsum(self, arr):  #Calculates the Sum of Subarray maximums
        n = len(arr)
        NGE = self.findNGE(arr)
        PGEE = self.findPGEE(arr)
        total = 0
        for i in range(n):
            left = i - PGEE[i]
            right = NGE[i] - i
            total += (left*right*arr[i])
        return total
    
    def smallestsum(self, arr): #Calculates the sum of subarray minimums
        n = len(arr)
        NSE = self.findNSE(arr)
        PSEE = self.findPSEE(arr)
        total = 0
        for i in range(n):
            left = i - PSEE[i]
            right = NSE[i] - i
            total += (left*right*arr[i])
        return total

    def findNGE(self, arr): #Calculates Next Greater element
        n = len(arr)
        NGE = [n]*n
        stack = []
        i = n-1
        while i >= 0:
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            if not stack:
                NGE[i] = n
            else:
                NGE[i] = stack[-1]
            stack.append(i)
            i -= 1
        return NGE

    def findPGEE(self, arr):    #Calculates Previous Greater or Equal element
        n = len(arr)
        PGEE = [-1]*n
        stack = []
        i = 0
        while i < n:
            while stack and arr[i] > arr[stack[-1]]:
                stack.pop()
            if not stack:
                PGEE[i] = -1
            else:
                PGEE[i] = stack[-1]
            stack.append(i)
            i += 1
        return PGEE

    def findNSE(self, arr): #Calculates Next Smaller Element
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

    def findPSEE(self,arr): #Calculates Previous Smaller or Equal Element
        n = len(arr)
        PSEE = [-1]*n
        stack = []
        i = 0
        while i < n:
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if not stack:
                PSEE[i] = -1
            else:
                PSEE[i] = stack[-1]
            stack.append(i)
            i += 1
        return PSEE