class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        NSE = self.findNSE(arr)     #Next Smaller Element
        PSEE = self.findPSEE(arr)   #Previous Smaller Element or Equal
        total, mod = 0, (10**9+7)

        for i in range(len(arr)):
            left = i - NSE[i]   #No of elements which are larger than arr[i] on the right
            right = PSEE[i] - i #No of elements which are larger than arr[i] on the left
            total = (total+(left*right*arr[i])%mod)%mod
        return total

    def findNSE(self, arr): #Returns the index of next smaller element in the array for each elemnt
        NSE = [len(arr)]*len(arr)
        stack = []
        i = len(arr)-1
        while i>=0:
            while stack and arr[i] <= arr[stack[-1]]:   #Stack also stores only indexes not the actual element
                stack.pop()
            if not stack:
                NSE[i] = len(arr)
            else:
                NSE[i] = stack[-1]
            stack.append(i)
            i -= 1
        return NSE

    def findPSEE(self, arr): #Returns the index of previous smaller or equal(To prevent duplication) element in the array for each element
        PSEE = [-1]*len(arr)
        stack = []
        i = 0
        while i<len(arr):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if not stack:
                PSEE[i] = -1
            else:
                PSEE[i] = stack[-1]
            stack.append(i)
            i += 1
        return PSEE