class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(n):
            if i == 0:
                prefix[i] = nums[i]
                suffix[-1 - i] = nums[-1 - i]
            else:
                prefix[i] = nums[i] * prefix[i - 1]
                suffix[-1 - i] = nums[-1 - i] * suffix[-i]

        res = []
        for i in range(n):
            if i == 0:
                res.append(suffix[i + 1])
            elif i == n - 1:
                res.append(prefix[i - 1])
            elif i > 0:
                res.append(prefix[i-1] * suffix[i+1])
            
        return res
