class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        prev = 0

        while l < r:
            a = heights[l]
            b = heights[r]
            print(a, b)
            volume = max(min(a, b) * (r - l), prev)
            prev = volume

            if a < b:
                l += 1
            else:
                r -= 1

        return volume           