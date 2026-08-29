class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hasharr = [-1]*256
        l, r, maxlen = 0, 0, 0
        while r<n:
            charcode = ord(s[r])
            if hasharr[charcode] != -1: #Means its in the hashmap
                if hasharr[charcode] >= l:  #l is already updated
                    l = hasharr[charcode]+1
            length = r-l+1
            maxlen = max(maxlen,length)
            hasharr[charcode] = r
            r += 1
        return maxlen