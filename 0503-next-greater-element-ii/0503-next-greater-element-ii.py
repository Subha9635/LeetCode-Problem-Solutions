class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        NGE = [0]*n
        i = 2*n-1

        while i>=0:
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i < n:
                if not stack:
                    NGE[i] = -1
                else:
                    NGE[i] = stack[-1]
            stack.append(nums[i%n])
            i -= 1
        
        return NGE