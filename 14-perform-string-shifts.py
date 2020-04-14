class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        t = 0
        for d, a in shift:
            t += a if d == 1 else -a
        ts = t % len(s)
        return s[-ts:] + s[:-ts]
