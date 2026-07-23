# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#iterative DFS
#keep stack with all left nodes as deep as possible
#pop val (this is the smallest), decrement k by 1
#if parent node has right child, add to stack, keep going as far left as possible again
#pop val (next smallest), decrement k by 1
#if parent has no right child, pop val again and decrement by one
#repeat if parent has right child/no right child
#until k == 0

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        count = k
        curr = root

        while stack or curr:
            while curr:
                if curr:
                    stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            curr = curr.right
            


        

    

