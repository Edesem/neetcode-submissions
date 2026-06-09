class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        i = (r - l) // 2
        res = -1

        while l <= r:
            if nums[i] == target:
                res = i
                break
            elif nums[i] > target:
                r = i - 1
                i = l + (r - l) // 2
            else:
                l = i + 1
                i = l + (r - l) // 2
        
        return res