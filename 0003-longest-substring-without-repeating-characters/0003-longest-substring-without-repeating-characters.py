class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlen = 0
        for i in range(n):
            hashmap = {}
            for j in range(i,n):
                if s[j] in hashmap:
                    break
                maxlen = max(maxlen,j-i+1)
                hashmap[s[j]] = 1
        return maxlen