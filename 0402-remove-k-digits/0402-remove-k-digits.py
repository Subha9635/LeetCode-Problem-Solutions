class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        
        stack = []  #Stores string
        i = 0
        res = ""
        while i < len(num):
            while stack and int(stack[-1]) > int(num[i]) and k>0:  #Poppes out bigger elements until k is still left
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while stack and k > 0:    #If k still remains ex- 123456
            stack.pop()
            k -= 1
        while stack:    #Putting stack elements in the res string
            res += stack.pop()
        
        res = res.rstrip("0")   #Removes 0's from the tail
        
        if not res: #In case res had all 0's
            return "0"

        return res[::-1]