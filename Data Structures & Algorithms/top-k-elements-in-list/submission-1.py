class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        res = []
        for _ in range(k):
            res.append(max(freq_map, key=freq_map.get))
            freq_map.pop(max(freq_map, key=freq_map.get))

        return res