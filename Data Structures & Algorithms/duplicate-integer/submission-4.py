class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if map.get(num) == None:
                map[num] = True
            else:
                return True

        return False