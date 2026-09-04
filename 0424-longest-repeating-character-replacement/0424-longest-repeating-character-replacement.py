class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hasharr = [0]*26
        l, r, maxlen, maxfreq = 0, 0, 0, 0
        while r<len(s):
            hasharr[ord(s[r])-ord('A')] += 1    #Freq gets updated
            maxfreq = max(maxfreq, hasharr[ord(s[r])-ord('A')])
            while (r-l+1)-maxfreq > k:
                hasharr[ord(s[l])-ord('A')] -= 1
                maxfreq = 0
                for i in range(26):
                    maxfreq = max(maxfreq,hasharr[i])
                l += 1
            if (r-l+1)-maxfreq <= k:
                maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen