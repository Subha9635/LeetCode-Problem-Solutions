from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxlen = 0
        mapp = defaultdict(int)
        l, r = 0, 0
        while r<len(fruits):
            mapp[fruits[r]] += 1
            if len(mapp) > 2:
                mapp[fruits[l]] -= 1
                if mapp[fruits[l]] == 0:
                    del mapp[fruits[l]]
                l += 1
            if len(mapp) <= 2:
                maxlen = max(maxlen,r-l+1)
            r += 1
        return maxlen
