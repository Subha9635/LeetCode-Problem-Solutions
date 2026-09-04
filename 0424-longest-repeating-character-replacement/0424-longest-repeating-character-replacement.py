class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hasharr = [0]*26
        l, r, maxlen, maxfreq = 0, 0, 0, 0
        while r<len(s):
            hasharr[ord(s[r])-65] += 1
            maxfreq = max(maxfreq, hasharr[ord(s[r])-65])
            if (r-l+1)-maxfreq>k:
                hasharr[ord(s[l])-65] -= 1
                l += 1
            else:
                maxlen = max(maxlen, r-l+1)
            r += 1
        return maxlen