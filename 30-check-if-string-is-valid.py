class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        return self.solve(root, arr, 0)
    
    def solve(self, root, arr, i):
        if root == None:
            return False
        if root.val == arr[i]:
            if i == len(arr) - 1:
                return root.left == None and root.right == None
            return self.solve(root.left, arr, i + 1) or self.solve(root.right, arr, i + 1)
        return False
