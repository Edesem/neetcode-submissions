class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if map.get(num) == None:
                map[num] = 2
            else:
                return True

        return False