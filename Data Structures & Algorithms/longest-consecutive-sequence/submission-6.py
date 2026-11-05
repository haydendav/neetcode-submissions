class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            length = 1 #local length to compare against current max
            if num - 1 in numSet:
                continue
            while num + length in numSet: #loop to find if the sequence exists
                length += 1
            longest = max(length, longest)
            
        return longest
            
