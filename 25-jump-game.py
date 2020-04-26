class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jumps_to_sln = 1
        
        for i in reversed(range(len(nums) - 1)):
            if nums[i] >= jumps_to_sln:
                jumps_to_sln = 1
            else:
                jumps_to_sln += 1
        return jumps_to_sln == 1
