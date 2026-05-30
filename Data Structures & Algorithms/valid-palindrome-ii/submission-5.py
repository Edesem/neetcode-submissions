class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            
            else:
                if s[l + 1] == s[r]:
                    ll = l + 1
                    rr = r
                    while ll < rr:
                        if s[ll] == s[rr]:
                            ll += 1
                            rr -= 1
                        else:
                            break
                    return True
                if s[l] == s[r - 1]:
                    ll = l 
                    rr = r - 1
                    while ll < rr:
                        if s[ll] == s[rr]:
                            ll += 1
                            rr -= 1
                        else:
                            return False
                    return True
                else:
                    return False
        
        return True
                
            