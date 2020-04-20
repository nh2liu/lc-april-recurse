class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.state = [0]
        return self.solve(preorder, None)
    
    def solve(self, preorder, upper_bound):
        i = self.state[0]
        if i >= len(preorder):
            return None
        v = preorder[i]
        if upper_bound == None or v <= upper_bound:
            node = TreeNode(v)
            self.state[0] += 1
            node.left = self.solve(preorder, v)
            node.right = self.solve(preorder, upper_bound)
            return node
        else:
            return None
