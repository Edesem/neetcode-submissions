class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        counter = 0
        length = len(flowerbed) - 1

        for i, flower in enumerate(flowerbed):
            # 3 tile
            if flower == 0:
                counter += 1
            else:
                counter = 0

            if length + 1 == 1 and counter == 1:
                res += 1
                
            elif counter == 2:
                plant_idx = None

                if i < length and flowerbed[i + 1] == 0:
                    plant_idx = i
                elif i == 1 and flowerbed[i - 1] == 0:
                    plant_idx = i - 1
                elif i == length and flowerbed[i - 1] == 0:
                    plant_idx = i

                if plant_idx is not None:
                    flowerbed[plant_idx] = 1
                    counter = 0
                    res += 1

        return res >= n
