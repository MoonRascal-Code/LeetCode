class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        table = collections.defaultdict(int)
        for i in s:
            table[i] +=1

        stack = [] 
        
        for char in s:
            table[char] -=1 
            if char in stack:
                continue
            while stack and stack[-1] > char and table[stack[-1]] !=0:
                stack.pop()
                print(stack)
            stack.append(char)

        return ''.join(stack)