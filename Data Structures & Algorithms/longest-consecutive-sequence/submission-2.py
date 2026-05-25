class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:
            #if there is not a number to the left it would be the start of a sequence
            if num-1 not in numSet:
                seqLength = 0
                while(num + seqLength) in numSet:
                    seqLength += 1
                longest = max(seqLength, longest)
        return longest