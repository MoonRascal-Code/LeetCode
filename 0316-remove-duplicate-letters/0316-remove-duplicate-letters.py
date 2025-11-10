class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # collections.Counter함수로 간단하게 만들 수 있음
        table = collections.defaultdict(int) 
        for i in s:
            table[i] +=1

        stack = [] 
        for char in s: 
            table[char] -=1 
            if char in stack: # set 자료형을 사용해서도 풀 수 있음 
                continue
            while stack and stack[-1] > char and table[stack[-1]] !=0:
                stack.pop()
                print(stack)
            stack.append(char)

        return ''.join(stack)