class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = defaultdict(int)

        for char in s:
            map[char] += 1

        for char in t:
            if map[char] > 0:
                map[char] -= 1
            else:
                return False

        return True