class Solution(object):
    def solve(self, root):
        if root == None:
            return (0, 0)
        else:
            ldepth, ldia = self.solve(root.left)
            rdepth, rdia = self.solve(root.right)
            
            new_depth = max(ldepth, rdepth) + 1
            new_dia = max(ldia, rdia, ldepth + rdepth)
            return (max(ldepth, rdepth) + 1, new_dia)
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.solve(root)[1]
