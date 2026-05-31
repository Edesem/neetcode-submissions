class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        prefix = [0] * n
        suffix = [0] * n

        for i in range(n):
            if i == 0:
                prefix[0] = nums[0]
                suffix[-1] = nums[-1]
            else:
                prefix[i] = nums[i] + prefix[i - 1]
                suffix[-1 - i] = nums[-1 - i] + suffix[-i]
        
        for i in range(n):
            print(i)
            if i == 0 and suffix[1] == 0:
                return 0
            elif i == n - 1 and prefix[n - 2] == 0:
                return n - 1
            elif i == n -1:
                return -1
            elif prefix[i - 1] == suffix[i + 1]:
                return i
                
