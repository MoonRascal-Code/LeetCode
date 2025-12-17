# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0 
        def dfs(node:TreeNode):
            # nonlocal longest # # ! 함수 내부에서 할당이 있으면 그 이름은 "지역 변수"로 간주된다. 
            # 종료 조건 및 패널티 
            if not node: 
                # ! None 에는 .val이 없기 때문에, node.val하면 오류가 발생 
                return -1 
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left+right+2) # 2는 현재 노드에서 좌우 노드 간선을 더해준 값
            # ! 함수 내부에서 할당이 있으면 그 이름은 "지역 변수"로 간주된다. 

            return max(left,right) +1 
            # -1 상쇄 목적의 +1 이기도 하면서 
            # 간선 하나의 길이 
        dfs(root)
        return self.longest 
            

