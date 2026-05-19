class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        dicts = []
        grouped = defaultdict(list)

        # O(m)
        for str in strs:
            dicts.append([0] * 26)

        # O(m * n)
        for i, str in enumerate(strs):
            dict = dicts[i]
            for char in str:
                dict[ord(char) - ord('a')] += 1
            grouped[tuple(dict)].append(str)

        return list(grouped.values())