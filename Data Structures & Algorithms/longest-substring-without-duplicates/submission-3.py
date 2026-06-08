class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        longest = 0
        l = 0
        r = 0
        chars = defaultdict(bool)

        while r < len(s):
            print(s[r])
            if s[r] not in chars:
                chars[s[r]] = True
                r += 1
                length += 1
                longest = max(longest, length)
            else:
                print("clear")
                chars.clear()
                l += 1
                r = l
                longest = max(longest, length)
                length = 0
        
        return longest
