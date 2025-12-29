# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # BFS 
        deque = collections.deque([root])
        result = ["#"] # 보통의 인덱스를 1부터 시작하게 한다. 
        # 역직렬화때 2의 배수가 depth가 되게 하기 위해 

        while deque:
            cur = deque.popleft()

            if cur: 
                result.append(str(cur.val))

                deque.append(cur.left)
                deque.append(cur.right)
            else:
                result.append("#")

        return " ".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "# #":
            return []
        
        seria = data.split()
        index = 2
        root =  TreeNode(int(seria[1]))
        deque = collections.deque([root])

        while deque:
            cur = deque.popleft()
            if seria[index] != "#":
                cur.left = TreeNode(seria[index])
                deque.append(cur.left)
            index +=1 

            if seria[index] != "#":
                cur.right = TreeNode(seria[index])
                deque.append(cur.right)
            index +=1 
        return root 


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))