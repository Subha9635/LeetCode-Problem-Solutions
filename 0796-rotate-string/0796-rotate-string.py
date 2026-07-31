class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        n = len(s)
        for i in range(n-1):
            rotated = s[i+1:n]+s[0:i+1]
            if rotated == goal:
                return True
        return False