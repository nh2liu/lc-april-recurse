class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        m, n = binaryMatrix.dimensions()
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            v = binaryMatrix.get(i,j)
            if v == 0:
                i -= 1
            else:
                j -= 1
        return -1 if j == n - 1 else j + 1
