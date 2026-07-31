class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        counter = 0
        for char in s:
            if char == "(":
                if counter > 0:
                    result += char
                counter += 1
            elif char == ")":
                counter -= 1
                if counter >0:
                    result += char
        return result