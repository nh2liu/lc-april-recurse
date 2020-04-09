class Solution(object):   
    def simplify(self, S):
        stack = []
        for s in S:
            if s == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(s)
        return ''.join(stack)
    
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.simplify(S) == self.simplify(T)
