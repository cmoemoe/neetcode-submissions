# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #BST to find node where p and q are both children
        #if direct child, LCA is parent node
        #if siblings, LCA is parent node
        #start at root bc it will be the CA of all nodes
        #if p and q are larger than root, look in left tree
        #if p and q are smaller than root, look in right tree
        #if p and q in diff subtrees, the root is LCA
        #if p or q == root, root is LCA

        if not root or not p or not q:
            return None

        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val): 
            return self.lowestCommonAncestor(root.right, p, q)
        else: #takes care of when p or q == root.val
            return root

        



