class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        prev_alnum = False

        while l < r:
            print(s[l].lower(), s[r].lower())
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                
            if not s[l].isalnum():
                l += 1
                prev_alnum = True
                continue
            else:
                prev_alnum = False
                
            if not s[r].isalnum():
                r -= 1
                prev_alnum = True
                continue
            else:
                prev_alnum = False
            
                
            if s[l].lower() != s[r].lower() and not prev_alnum:
                return False
            
                
        return True