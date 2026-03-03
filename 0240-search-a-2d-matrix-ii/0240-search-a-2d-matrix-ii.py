class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        row = 0
        col = len(matrix[0])-1

        while row <= len(matrix) -1 and col >=0:
            if matrix[row][col] < target:
                row +=1 
            elif matrix[row][col] > target:
                col -=1 
            else: 
                return True 
        return False