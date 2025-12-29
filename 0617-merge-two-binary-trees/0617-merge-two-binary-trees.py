# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2 
        if root2 is None:
            return root1 
        
        que = collections.deque()
        que.append((root1,root2))

        while que:
            # print(que.popleft()
            n1,n2 = que.popleft()

            n1.val += n2.val

            if n1.left and n2.left:
                que.append((n1.left,n2.left))
            elif not n1.left:
                n1.left = n2.left
                # n1 을 반환할꺼기 때문에, n2없는 경우는 신경안써도 된다. 

            if n1.right and n2.right:
                que.append((n1.right,n2.right))
            elif not n1.right:
                n1.right = n2.right 
            
        return root1