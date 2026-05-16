class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        looking_for = 0

        for idx, num in enumerate(nums):
            a = dict.get(num)
            if a != None:
                return [a, idx] 

            dict[target - num] = idx
