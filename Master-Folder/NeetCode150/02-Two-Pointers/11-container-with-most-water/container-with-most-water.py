class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        heights given, breadth given by indices 

        """
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right-left) * min(height[left], height[right])
            result = max(result, area)
            if height[left] > height[right]:
                right -= 1
            # if height[left] < height[right]:
            #     left += 1
            else:
                left += 1 
        return result