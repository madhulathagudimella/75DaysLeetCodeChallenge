# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 🔹 Iterative Approach
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # If both nodes are smaller → go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # If both nodes are greater → go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # Otherwise → this is the LCA
            else:
                return root


    # 🔹 Recursive Approach (alternative)
    def lowestCommonAncestorRecursive(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorRecursive(root.left, p, q)
        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorRecursive(root.right, p, q)
        
        return root