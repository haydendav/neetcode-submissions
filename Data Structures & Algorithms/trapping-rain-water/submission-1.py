class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0

        for i in range(len(height)):
            left_max = max(height[:i+1])
            right_max = max(height[i:])
            water = min(left_max, right_max) - height[i]
            trapped += water

        return trapped