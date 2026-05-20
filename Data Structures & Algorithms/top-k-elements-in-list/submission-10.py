class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq_map = defaultdict(list)

        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            freq_map[freq].append(num)
        
        res = []
        max_freq = max(freq_map)
        for i in range(k + 1):
            if freq_map[max_freq - i]:
                res.extend(freq_map[max_freq - i][:k])
                if len(res) == k:
                    break

        return res