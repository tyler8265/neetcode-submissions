class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = []
        while left < right:
            if heights[left] < heights[right]:
                height = heights[left]
            else:
                height = heights[right]
            width = right - left
            curArea = width * height
            print(curArea)
            if len(res) < 1 or curArea > res[0]:
                res.insert(0, curArea)
            else:
                res.append(curArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res[0]