# Container With Most Water
# Pattern: Two Pointers
# Difficulty: Medium

def maxWater(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, (right - left) * min(heights[left], heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area
