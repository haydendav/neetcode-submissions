class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            temp = nums[:]
            temp[i] = 1
            ans = 1
            for nim in temp:
                ans *= nim
            res.append(ans)

        return res
        