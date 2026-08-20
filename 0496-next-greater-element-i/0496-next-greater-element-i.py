class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        NGE = [0]*len(nums2)
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<=nums2[i]:
                stack.pop()
            if not stack:
                NGE[i] = -1
            else:
                NGE[i] = stack[-1]
            stack.append(nums2[i])

        nge_map = {nums2[i]:NGE[i] for i in range(len(nums2))} #Creting a hashmap to retrieve NGE in O(1)

        return [nge_map[num] for num in nums1]