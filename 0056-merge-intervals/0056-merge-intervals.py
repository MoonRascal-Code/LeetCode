class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = [] 
        # 1. 첫번째 요소로 정렬 
        for i in sorted(intervals, key=lambda x : x[0]):
            # 2. 이전 범위 마지막과 현재 범위 첫번쨰 요소를 비교 
            if result and i[0] <= result[-1][1]:
                # 2-1. 범위가 겹치면 merge  
                result[-1][1] = max(result[-1][1],i[-1]) # max 빼먹음 
                # 2-1. 아니면 결과 list 에 추가 
            else:
                result.append(i)
        return result 