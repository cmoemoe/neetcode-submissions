# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS through the subtrees until violates condition
#left node < root
#right node > root
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l, r = -math.inf, math.inf

        return self.binSearch(root, l, r)

    def binSearch(self, root, l, r):
        if not root:
            return True

        if root.val < r and root.val > l:
            return self.binSearch(root.left, l, root.val) and self.binSearch(root.right, root.val, r)
        else:
            return False
