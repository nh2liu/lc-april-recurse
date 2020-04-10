class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.main_stack.append(x)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        x = self.main_stack.pop()
        if self.min_stack[-1] == x:
            self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.main_stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
