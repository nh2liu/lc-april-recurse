class Solution(object):
    def maxPathSum(self, root):
        return self.solve(root)[0]
    
    def solve(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return (-float('inf'), 0)
        lmax, lpath = self.solve(root.left)
        rmax, rpath = self.solve(root.right)
        
        cpath = max(lpath, rpath, 0) + root.val
        cmax = max(lmax, rmax, max(lpath, 0) + max(rpath, 0) + root.val)
        return cmax, cpath
