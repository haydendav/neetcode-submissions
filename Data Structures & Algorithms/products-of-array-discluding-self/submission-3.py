class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1] #multiply everything on left

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #multiply everything on right
            res[i] *= postfix #by using a postfix value that updates as the product of everything seen so far
            postfix *= nums[i]

        return res