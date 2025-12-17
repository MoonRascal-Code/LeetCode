# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 

        # 일반적인 BFS
        queue = collections.deque([root])
        depth = 0 

        while queue: 
            depth +=1 
            for _ in range(len(queue)):
                # TN(3)
                cur_root = queue.popleft()
                if left:=cur_root.left:
                    queue.append(left)
                if right:=cur_root.right:
                    queue.append(right)
        return depth