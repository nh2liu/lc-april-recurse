class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        a = set(arr)
        for v in arr:
            if v + 1 in a:
                count += 1
        return count
