class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r,count = 0,0,0
        minlen = float("inf")
        start = -1
        hash = {}
        for char in t:  #Prestoring chars of t in hashmap
            hash[char] = hash.get(char,0)+1
        
        while r < len(s):
            if s[r] in hash:
                if hash[s[r]] > 0:  #Already in the hashmap from t
                    count += 1
                hash[s[r]] -= 1
            while count == len(t):
                if (r-l+1)<minlen:
                    minlen = r-l+1
                    start = l
                if s[l] in hash:
                    hash[s[l]] += 1
                    if hash[s[l]]>0:
                        count -= 1
                l += 1
            r += 1
        return "" if start == -1 else s[start:start+minlen]