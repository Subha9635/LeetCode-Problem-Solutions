class Solution:
    def beautySum(self, s: str) -> int:
        totalbeauty = 0
        n = len(s)

        for i in range(n):
            freq = [0]*26
            for j in range(i,n):
                freq[ord(s[j])-ord("a")] += 1
                maxfreq, minfreq = 0, float("inf")
                for count in freq:
                    if count>0:
                        if count < minfreq:
                            minfreq = count
                        if count > maxfreq:
                            maxfreq = count
                totalbeauty += (maxfreq-minfreq)
        return totalbeauty