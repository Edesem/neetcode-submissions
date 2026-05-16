class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 1
        best = 1

        if len(nums) == 0:
            longest = 0
            return longest

        for num in numSet:
            longest = 1
            if num - 1 not in numSet:
                numCurrent = num
                while numCurrent + 1 in numSet:
                    longest += 1
                    numCurrent += 1

                if longest > best:
                    best = longest
                
        print(numSet)

        print(best)
        return best