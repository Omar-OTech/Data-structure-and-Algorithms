# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        # step 1: Base Case
        if root is None:
            return 0
        
        # Step 2: Initialize the sum
        left_sum = 0
        
        # Step 3: Check if the left child is a leaf
        if root.left and root.left.left is None and root.left.right is None:
            left_sum += root.left.val
        
        # Step 4: Recursively sum left leaves in both subtrees
        left_sum += self.sumOfLeftLeaves(root.left)
        left_sum += self.sumOfLeftLeaves(root.right)
        
        return left_sum



# Tree: [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

sol = Solution()
print(sol.sumOfLeftLeaves(root))  # Output: 24
