class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        longest = 0
        l = 0
        r = 0
        chars = set()

        while r < n:
            print(l, r, s[l], s[r])
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest
