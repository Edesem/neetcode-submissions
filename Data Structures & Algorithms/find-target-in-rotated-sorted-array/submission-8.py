class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            print(nums[l], nums[mid], nums[r])

            if nums[mid] == target:
                return mid

            # Left sorted
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right sorted
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid + 1        
                else:
                    r = mid - 1

        return -1