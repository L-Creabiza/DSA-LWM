class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left<right:
            cum = numbers[left] + numbers[right]
            if cum == target:
                return [left+1, right+1]
            elif cum < target:
                left += 1
            else:
                right -= 1