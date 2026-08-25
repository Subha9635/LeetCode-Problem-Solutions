from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        deque is used here because it allows elements to be pushed and popped
        from both end
        '''
        dq = deque()
        result = []

        for i in range(len(nums)):
            if dq and dq[0] <= i-k: 
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:   #Poppes out element from the back to maintain monotonic decreasing order
                dq.pop()
            dq.append(i)
            if i >= k-1:    #When window size goes beyond k, element from the first gets removed
                result.append(nums[dq[0]])
        return result