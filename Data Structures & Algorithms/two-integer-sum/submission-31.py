class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in complements:
                return [complements[needed], i]
            complements[num] = i
        