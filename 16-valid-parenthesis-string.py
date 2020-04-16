class Solution(object):    
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = 0
        for c in s:
            if c in '(*':
                l += 1
            else:
                l -= 1
            if l < 0:
                return False
        
        for c in reversed(s):
            if c in ')*':
                r += 1
            else:
                r -= 1
            if r < 0:
                return False
        return True
        
