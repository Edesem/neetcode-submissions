class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        stack = list(s)
        if not stack:
            return True

        for i in range(len(t)):
            print(stack)
            if t[-1 - i] == stack[-1]:
                stack.pop()
                if not stack:
                    return True
        
        if not stack:
            return True
        else:
            return False
        