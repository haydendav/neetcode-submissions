class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        #left
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1] #multiply everything to the left and whatever is on the left is already multiplied by everything else

        #right
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res