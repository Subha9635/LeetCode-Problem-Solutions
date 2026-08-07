class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.dfs(num,target,0,0,0,"",res)
        return res

    def dfs(self, num, target, start, current_value, last_operand, expression, result):
        # Base case: If we've reached the end of the string
        if start == len(num):
            # If the expression evaluates to the target
            if current_value == target:  
                result.append(expression)
            return
        
        # Loop through all substrings starting from 'start' index
        for i in range(start, len(num)):
            # Skip leading zeros in numbers
            if i > start and num[start] == '0':
                return
            
            # Get the current number
            current_num = num[start:i+1]  
            # Convert current number to integer
            current_num_val = int(current_num)  
            
            # If we are at the first number, just start the expression
            if start == 0:
                self.dfs(num, target, i + 1, current_num_val, current_num_val, current_num, result)
            else:
                # Add the current number with '+'
                self.dfs(num, target, i + 1, current_value + current_num_val, current_num_val, expression + "+" + current_num, result)
                
                # Add the current number with '-'
                self.dfs(num, target, i + 1, current_value - current_num_val, -current_num_val, expression + "-" + current_num, result)
                
                # Add the current number with '*'
                self.dfs(num, target, i + 1, current_value - last_operand + last_operand * current_num_val, last_operand * current_num_val, expression + "*" + current_num, result)