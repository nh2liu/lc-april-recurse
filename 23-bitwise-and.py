class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        k = 0
        while n != m:
            n >>= 1
            m >>= 1
            k += 1
        return n << k
