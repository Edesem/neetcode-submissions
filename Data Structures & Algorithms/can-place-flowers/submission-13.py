class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        counter = 0
        length = len(flowerbed) - 1

        for i, flower in enumerate(flowerbed):
            if flower == 0:
                counter += 1
            else:
                counter = 0

            # Single element case
            if len(flowerbed) == 1 and counter == 1:
                return n <= 1

            elif counter == 2:
                if (
                    (i < length and flowerbed[i + 1] == 0)
                    or (i == 1 and flowerbed[i - 1] == 0)
                    or (i == length and flowerbed[i - 1] == 0)
                ):
                    counter = 0
                    res += 1

        return res >= n
