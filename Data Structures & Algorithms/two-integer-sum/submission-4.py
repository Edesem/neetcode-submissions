class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for idx, num in enumerate(nums):
            diff = map.get(num)
            if diff != None:
                return [diff, idx] 

            map[target - num] = idx
