class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        first_alnum = False
        for i in range(len(s)):
            if s[-1 - i].isalnum():
                first_alnum = True
                length += 1
                continue
            elif not first_alnum and s[-1 - i] == " ":
                continue
            else:
                return length

        return length