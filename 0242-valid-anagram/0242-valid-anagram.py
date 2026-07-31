class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq = [0]*26
        for char in s:   #Increases the counter value for that alphabet in the freq array
            freq[ord(char)-ord('a')] += 1
        for char in t:   #Decreases the counter value for that alphabet in the freq array
            freq[ord(char)-ord('a')] -= 1
        for count in freq:
            if count != 0:
                return False
        return True