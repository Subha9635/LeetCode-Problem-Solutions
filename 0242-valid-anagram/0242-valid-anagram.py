class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        if s==t:
            return True
        return sorted(s) == sorted(t)