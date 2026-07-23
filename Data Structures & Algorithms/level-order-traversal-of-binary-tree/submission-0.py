# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS
#queue represents layers

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = collections.deque()
        queue.append(root)

        while queue:
            qLen = len(queue)
            lvl = []
            for i in range(qLen):
                node = queue.popleft()
                if node:
                    lvl.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if lvl:
                res.append(lvl)
    
        return res

        
            

            

            