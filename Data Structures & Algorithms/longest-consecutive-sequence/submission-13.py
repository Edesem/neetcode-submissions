class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        seq = set(nums)
        mp = {}
        longest = 1

        for num in seq:
            if num - 1 not in seq:
                i = 1
                while num + i in seq:
                    print(num)
                    longest += 1
                    i += 1
                mp[num] = longest
                longest = 1

        return max(mp.values())
                    
