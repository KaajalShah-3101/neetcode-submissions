class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        best = 0
        while left < right:
            width = right - left
            height = min(heights[right], heights[left])
            best = max(best, width * height)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return best
        