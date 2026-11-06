class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for i, num in enumerate(numSet):
            current = 1
            if num - 1 in numSet:
                continue
            while num + current in numSet:
                current += 1
            
            longest = max(longest, current)

        return longest