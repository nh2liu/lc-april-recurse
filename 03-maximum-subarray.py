class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_so_far = 0
        sum_so_far = 0
        sln = nums[0]
        for num in nums:
            sum_so_far += num
            if sum_so_far - min_so_far > sln:
                sln = sum_so_far - min_so_far
            if sum_so_far < min_so_far:
                min_so_far = sum_so_far
        return sln
            
