class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = []
        for num in nums:
            if num not in copy:
                copy.append(num)
            else:
                return True
        return False
         