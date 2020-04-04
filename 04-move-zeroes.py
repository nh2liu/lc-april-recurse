class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i1 = 0
        i2 = 0
        while i1 < len(nums) and i2 < len(nums):
            v1, v2 = nums[i1], nums[i2]
            if v1 == 0 and v2 != 0:
                nums[i1] = v2
                nums[i2] = 0
                i2 += 1
                i1 += 1
            else:
                if v1 != 0:
                    i1 += 1
                if v2 == 0 or i1 > i2:
                    i2 += 1
            
