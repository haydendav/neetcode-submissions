class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeat = set()
        for num in nums: 
            if num in repeat:
                return True 
            repeat.add(num)
        return False
        