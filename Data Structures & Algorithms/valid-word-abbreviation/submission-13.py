class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool: 
        i = 0
        j = 0

        while j < len(abbr):
            if i >= len(word):
                return False

            w_char = word[i]
            a_char = abbr[j]
            if w_char == a_char:
                i += 1
                j += 1
            
            elif a_char.isdigit():
                if int(a_char) == 0:
                    return False

                length = ""
                while j < len(abbr) and abbr[j].isdigit():
                    length += abbr[j]
                    j += 1
                
                i += int(length)
            
            else:
                return False

        if i == len(word):
           return True
        return False
