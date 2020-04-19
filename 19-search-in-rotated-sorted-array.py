class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        l, r = 0, len(nums)
        while True:
            if r - l == 1:
                return l if nums[l] == target else -1

            mid = (l + r) // 2

            al, am = nums[l], nums[mid]
            if (al > am and (target >= al or target < am)) or \
                (target >= al and target < am):
                l, r = l, mid
            else:
                l = mid
        
