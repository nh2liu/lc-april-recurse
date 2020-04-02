class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = set([n])
        while True:
            if n == 1:
                return True
            else:
                new_n = 0
                while n > 0:
                    remainder = n % 10
                    n = n // 10
                    new_n += remainder * remainder
                if new_n in history:
                    return False
                n = new_n
                history.add(n)
