class Solution:
    def isValid(self, s: str) -> bool:
        if not s or len(s) <=1:
            return False

        table = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = [] 
        for char in s:
            if char not in table.keys():
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False 
        return len(stack) == 0

        
        