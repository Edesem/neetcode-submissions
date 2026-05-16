class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(num)
            else:
                prefix.append(num * prefix[i-1])

        postfix = [1] * len(nums)
        for i in range(1, len(nums) + 1):
            num = nums[-i]
            if i == 1:
                postfix[-i] = nums[-i]
            else:
                postfix[-i] = num * postfix[-i + 1]

        res = []
        for i in range(len(nums)):
            if i < 1:
                res.append(postfix[i + 1])
            elif i >= len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1] * postfix[i + 1])

        return res