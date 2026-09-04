class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        lastseen = [-1,-1,-1]
        for i in range(len(s)):
            lastseen[ord(s[i])-ord('a')] = i
            if lastseen[0] != -1 and lastseen[1] != -1 and lastseen[2] != -1:   #It means all of them are available; this check can be omitted as if it is not valid the min in the next step would be -1 which would keep the count as it is
                count += (1+min(lastseen))
        return count