class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        lsum = 0
        rsum = 0
        for i in range(k):  #Adding k elements from the front
            lsum += cardPoints[i]
        maxsum = lsum
        rindex = len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            rindex -= 1
            maxsum = max(maxsum,lsum+rsum)

        return maxsum