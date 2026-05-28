class Solution:
    def maxArea(self, heights: List[int]) -> int:
        biggest = 0

        left, right = 0, len(heights) - 1

        while left < right:
            biggest = max(biggest, ((right - left) * min(heights[left], heights[right])))

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return biggest