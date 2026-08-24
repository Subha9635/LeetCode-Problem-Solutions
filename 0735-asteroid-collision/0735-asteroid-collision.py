class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if asteroids[i] > 0:    #Explicitly mentioned that the value cant be 0
                stack.append(asteroids[i])  #only positive values gets straight away pushed into the stack
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):  #For smaller positive asteroids than current negative asteroid explodes the smaller one
                    stack.pop()
                if stack and stack[-1] == abs(asteroids[i]):    #For negative elements having same mass as stack top positive they both explodes
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroids[i])
            i += 1
        return stack