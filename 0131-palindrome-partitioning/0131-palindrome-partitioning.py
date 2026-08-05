class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []


        def isPalindrome(sub:str):
            return sub == sub[::-1]

        def partitioner(start:int):
            if start == len(s):
                res.append(path.copy())
                return
            for end in range(start+1,len(s)+1):
                if isPalindrome(s[start:end]):
                    path.append(s[start:end])
                    partitioner(end)
                    path.pop()
                
        partitioner(0)
        return res