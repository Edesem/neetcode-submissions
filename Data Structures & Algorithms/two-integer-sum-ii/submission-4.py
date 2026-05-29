class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            a = numbers[l]
            b = numbers[r]
            total = a + b

            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []