class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in complements:
                return [complements[need], i]
            complements[num] = i

        