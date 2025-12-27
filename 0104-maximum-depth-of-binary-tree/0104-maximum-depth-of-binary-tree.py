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
        # BFS 
        # deque 
        que = collections.deque([root])
        depth = 0 

        while que:
            depth +=1 
            for _ in range(len(que)): # len(que)는 고정된 값임 
                cur = que.popleft()
                print(cur.val, depth)
                if cur.left:
                    que.append(cur.left) # 9 
                if cur.right:
                    que.append(cur.right) # 20 

        return depth 

