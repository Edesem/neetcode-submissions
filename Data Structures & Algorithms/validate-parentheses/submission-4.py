class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        last_char = ""
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in "({[":
                stack.append(char)
                last_char = char
            if char in ")}]":
                if not stack:
                    return False

                element = stack.pop()
                if pairs[char] != element:
                    return False
        
        if len(stack) > 0:
            return False
        else:
            return True
