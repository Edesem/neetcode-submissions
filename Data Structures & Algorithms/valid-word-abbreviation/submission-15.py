class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool: 
        i = 0
        j = 0

        while j < len(abbr):
            a_char = abbr[j]
            if i < len(word) and word[i] == a_char:
                i += 1
                j += 1
            
            elif a_char.isdigit():
                if int(a_char) == 0:
                    return False

                length = 0
                while j < len(abbr) and abbr[j].isdigit():
                    length = length * 10 + int(abbr[j])
                    j += 1
                
                i += length
            
            else:
                return False

        return i == len(word)
