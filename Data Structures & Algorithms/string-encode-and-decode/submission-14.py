class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) != 0:
            res = ""
        else:
            return " "
            
        for i, string in enumerate(strs):
            if i < len(strs) - 1:
                res += string + ";SEPERATE;"
            else:
                res += string

        return res

    def decode(self, s: str) -> List[str]:
        if s == " ":
            return []
        else:
            return s.split(";SEPERATE;")
