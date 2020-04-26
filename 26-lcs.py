class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        D = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                D[i + 1][j + 1] = max(D[i][j] + int(c1 == c2), D[i + 1][j], D[i][j + 1]) 
        return D[-1][-1]
