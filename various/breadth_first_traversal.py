  
"""
You are given a binary tree.
Write a function that can return the inorder traversal of node values.
Example:
Input:
   3
    \
     1
    /
   5
Output: [3,5,1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    # Your code here
    def iter_depth_first_traverse(root):
        if root is None:
            return []

        result = []

        stack = []

        stack.append(root)

        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result