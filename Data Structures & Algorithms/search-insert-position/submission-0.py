class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = (r - l) // 2

        while l <= r:
            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = i + 1
                i = l + (r - l) // 2
            else:
                r = i - 1
                i = l + (r - l) // 2
            
        return i + 1