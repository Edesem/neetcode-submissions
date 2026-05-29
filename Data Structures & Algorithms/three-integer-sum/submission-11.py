class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(nums)
        res = []

        for i, num in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            a = num
            target = -a
            l = i + 1
            r = n - 1

            while l < r:
                b = sorted_nums[l]
                c = sorted_nums[r]
                total = b + c

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append([a, b, c])
                    l += 1
                    r -= 1

                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1

                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1


        return res
