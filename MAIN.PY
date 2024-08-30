class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)
        
        # Initialize variables
        self.prev = None
        self.first = None
        self.second = None
        
        # Perform the inorder traversal and find the two nodes that are out of order
        inorder(root)
        
        # Swap the values of the two identified nodes to recover the tree
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val

# Example usage:
solution = Solution()
# Construct example trees
root1 = TreeNode(1, None, TreeNode(3, TreeNode(2)))
solution.recoverTree(root1)
# Output should be the corrected tree [3,1,null,null,2]

root2 = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
solution.recoverTree(root2)
# Output should be the corrected tree [2,1,4,null,null,3]
