class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 문제 본질 
        # 패턴 파악 : 트리형태로 모든 경로를 탐색하는 DFS 
        # 알고리즘 설계 
        # 1. 현재 인덱스의 숫자를 하나 가져오고, 
        # 2. 그 숫자에 대한 문자 리스트를 반복하며, 
        # 3. 각 문자를 현재 문자열에 추가 
        # 4. 다음 숫자로 넘어감(재귀)
        # 5. 문자열 길이가 digits 길이와 같으면 결과에 추가 
        # 6. 돌아와서 다음 문자를 붙여보며 탐색 

        if not digits:
            return [] 
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(index,path):
            if len(path) == len(digits):
                result.append(path)
                return 

            for s in phone[digits[index]]:
                dfs(index+1,path+s)
        result = [] 
        dfs(0,'')

        return result 
