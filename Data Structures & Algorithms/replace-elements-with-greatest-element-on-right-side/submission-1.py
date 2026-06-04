class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffix_max = [0] * len(arr)

        max_so_far = -1
        for i in range(len(arr)):
            suffix_max[-1 - i] = max_so_far
            max_so_far = max(max_so_far, arr[-1 - i])

        return suffix_max