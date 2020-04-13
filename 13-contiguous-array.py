class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {0:-1}
        p = 0
        ret = 0
        for i, v in enumerate(nums):
            p += v * 2 - 1
            if p in h:
                ret = max(ret, i - h[p])
            else:
                h[p] = i
        return ret

