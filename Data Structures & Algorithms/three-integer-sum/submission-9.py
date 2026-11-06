class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for pos, value in enumerate(nums):
            if value > 0: #any future positive will not add up to 0
                break

            if pos > 0 and value == nums[pos - 1]: #if last value is same as this one skip
                continue 
            
            l, r = pos + 1, len(nums) - 1 

            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: 
                    res.append([value, nums[l], nums[r]]) 
                    r -= 1 #have to check the other options before exiting this current value 
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return res