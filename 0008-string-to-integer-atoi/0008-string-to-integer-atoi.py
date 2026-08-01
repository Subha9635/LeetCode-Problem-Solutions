class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  #Removes whitespaces
        if not s:
            return 0

        sign, index = 1, 0  #Checks for sign and tracks index
        if s[0] == "-":
            sign = -1
            index += 1
        elif s[0] == "+":
            index += 1
        INT_MIN, INT_MAX = -(2**31), 2**31-1
        result = 0

        while index<len(s) and s[index].isdigit():
            digit = int(s[index])
            if result > (INT_MAX - digit)//10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result *10 + digit
            index += 1
        return sign*result