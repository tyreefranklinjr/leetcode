# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        """
        Utilizes a unique self function to check for
        'NoneType' and unequal values in each branch,
        checking for the next node in the BTS
        """
 
        if not p and not q: return True
        elif not p or not q: return False
        elif p.val != q.val: return False

        return (self.isSameTree(p.left, q.left) and (self.isSameTree(p.right, q.right)))

        # Time Complexity -> O(P + Q) as p and and q are the number of values in each element
        # Space Complexity -> O(1) as the auxillary space remains constant
