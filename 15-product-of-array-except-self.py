class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        F = [1] * n
        B = [1] * n
        for i in range(1, n):
            F[i] = F[i - 1] * nums[i - 1]
        
        for i in reversed(range(n - 1)):
            B[i] = B[i + 1] * nums[i + 1]
        
        return [F[i] * B[i] for i in range(n)]
