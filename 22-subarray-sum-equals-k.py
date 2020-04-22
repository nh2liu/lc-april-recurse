class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = defaultdict(int)
        t = 0
        ret = 0
        for i, v in enumerate(nums):
            t += v
            ret += d[t - k]
            d[t] += 1
        ret += d[k]
        return ret
