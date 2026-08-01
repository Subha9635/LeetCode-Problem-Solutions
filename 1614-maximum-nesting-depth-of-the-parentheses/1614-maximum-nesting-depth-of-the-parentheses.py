class Solution:
    def maxDepth(self, s: str) -> int:
        count, maxcount = 0, 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            if count > maxcount:
                maxcount = count
        return maxcount