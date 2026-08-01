class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        start, maxlen = 0, 0

        def expand(left,right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1
        
        for i in range(len(s)):
            len1 = expand(i,i)
            len2 = expand(i,i+1)
            currmax = max(len1,len2)
            if currmax > maxlen:
                maxlen = currmax
                start = i-(currmax-1)//2
        return s[start:start+maxlen]