# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        i = (r - l) // 2

        while l <= r:
            res = guess(i)
            if res == 0: 
                break
            elif res == 1:
                l = i + 1
                i = l + (r - l) // 2
            else:
                r = i - 1
                i = l + (r - l) // 2

        return i