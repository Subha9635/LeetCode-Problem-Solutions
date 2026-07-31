class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s==goal:
            return True
        check = s+s
        if goal in check:
            return True
        return False